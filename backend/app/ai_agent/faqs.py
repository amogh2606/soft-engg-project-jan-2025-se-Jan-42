from flask_restful import Resource, fields, marshal
from flask_security import roles_accepted
from app.models import db, Message, FAQs
from datetime import datetime

from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI



class FAQsResource(Resource):
    # get latest FAQs
    @roles_accepted('instructor', 'admin')
    def get(self):
        response_fields = {
            'rank': fields.Integer,
            'question': fields.String,
            'last_updated': fields.String
        }
        stmt = db.select(FAQs)
        faqs = db.session.scalars(stmt).all()

        return marshal(faqs, response_fields, envelope='faqs')



# generate and update FAQs
def update_faqs():
    print(f"[{datetime.now()}] Updating FAQs...")

    stmt = db.select(Message.text).filter_by(is_response=False)
    all_queries = db.session.scalars(stmt).all()

    # if not enough queries to generate FAQs
    if len(all_queries) <= 10:
        updated_faqs = [{"rank": i, "question": query} for i, query in enumerate(all_queries, start=1)]
    
    else:    
        prompt = PromptTemplate(
            template="""Based on the given queries from students,
                generate a list of top 10 FAQs concisely along with their ranks
                query_history: \n{queries}""",
            input_variables=["queries"]
        )
        llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-001',
            temperature=0
        )
        # pydantic data structure
        class FAQ(BaseModel):
            rank: int = Field(description="Rank of the FAQ", ge=1, le=10)
            question: str = Field(description="The question")
        class FAQList(BaseModel):
            faqs: list[FAQ] = Field(description="List of 10 FAQs", max_length=10)

        structured_llm = llm.with_structured_output(FAQList)
        chain = prompt | structured_llm
        
        try:
            output = chain.invoke({"queries": all_queries})
        except Exception as e:
            print(f"[{datetime.now()}] Failed to generate FAQs")
            print(e)
            return
        
        updated_faqs = output.model_dump().get('faqs')
    
    # replace updated FAQs in db
    stmt = db.delete(FAQs)
    db.session.execute(stmt)
    db.session.flush()

    for faq in updated_faqs:
        db.session.add(FAQs(rank=faq['rank'], question=faq['question']))
    
    db.session.commit()

