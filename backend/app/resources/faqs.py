from flask_restful import Resource
from flask_security import roles_accepted
from flask import jsonify
from app.models import db, Message

from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI



class GenerateFAQs(Resource):
    @roles_accepted('instructor', 'admin')
    def get(self):
        all_queries = self.get_query_history()
        # not enough queries to generate FAQs
        if len(all_queries) <= 10:
            return jsonify(faqs=all_queries)
        
        # pydantic data structure
        class FAQList(BaseModel):
            faqs: list[str] = Field(title="List of FAQs", max_length=10)

        json_parser = JsonOutputParser(pydantic_object=FAQList)

        prompt = PromptTemplate(
            template="""Based on the given queries from students,
                generate a list of top 10 concise FAQs in the given format.
                {format_instructions}\n{queries}""",

            input_variables=["queries"],
            partial_variables={"format_instructions": json_parser.get_format_instructions()},
        )
        llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-001',
            temperature=0
        )
        chain = prompt | llm | json_parser
        response = chain.invoke({"queries": all_queries})

        return response
    

    def get_query_history(self):
        stmt = db.select(Message.text).filter_by(is_response=False)
        return db.session.scalars(stmt).all()
