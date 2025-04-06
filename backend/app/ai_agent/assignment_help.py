from flask_restful import Resource, reqparse, marshal_with, fields, abort
from flask_security import auth_required, current_user
from app.models import db, Chat, Message, Course, Question
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from app.ai_agent.embeddings import client, embedding_function



parser = reqparse.RequestParser(trim=True)
parser.add_argument('question_id', type=int, required=True, nullable=False)
parser.add_argument('assignment_id', type=int, required=True, nullable=False)
parser.add_argument('course_id', type=int, required=True, nullable=False)

response_fields = {
    'chat_id': fields.Integer,
    'timestamp': fields.String,
    'message': fields.String(attribute='text')
}

class AssignmentHelp(Resource):
    @auth_required('session')
    @marshal_with(response_fields)
    def post(self):
        args = parser.parse_args()
        question_id = args.get('question_id')
        assignment_id = args.get('assignment_id')
        course_id = args.get('course_id')

        stmt = db.select(Question).filter_by(id=question_id, assignment_id=assignment_id)
        question = db.session.scalar(stmt)
        if not question:
            abort(404, message="Question not found")

        question_string = f"{question.text}\nA) {question.option_1}\nB) {question.option_2}\nC) {question.option_3}\nD) {question.option_4}"

        response = self.generate_response(question_string, question.correct_option, course_id)

        # Start a a new chat session
        stmt = db.select(Chat).filter_by(user_id=current_user.id, active=True)
        active_sessions = db.session.scalars(stmt)
        if active_sessions:
            for session in active_sessions:
                session.active = False

        new_chat = Chat(user_id=current_user.id, title="Assignment Help")
        db.session.add(new_chat)
        db.session.commit()

        # Save the question and response to db
        user_query = Message(chat_id=new_chat.id, text=question_string, is_response=False)
        ai_response = Message(chat_id=new_chat.id, text=response, is_response=True)
        
        db.session.add_all([user_query, ai_response])
        db.session.commit()

        return ai_response
    

    def generate_response(self, question, correct_option, course_id=None):
        if course_id:
            db.get_or_404(Course, course_id, description="Course not found")
            
        collection_name = f'course_{course_id}' if course_id else 'general'
        try:
            vector_store = Chroma(
                collection_name=collection_name,
                embedding_function=embedding_function,
                client=client,
                create_collection_if_not_exists=False
            )
            retriever = vector_store.as_retriever()
            res = retriever.invoke(question)
            relevant_docs = '\n\n'.join(set(doc.page_content for doc in res))
        except:
            relevant_docs = ""
        
        prompt_template = ChatPromptTemplate([
            ("system", """You are a chatbot in an e-learning platform helping a student with an assignment question.
                In this entire conversation, don't reveal the answer in any case, which is option {correct_option}.
                Instead you can provide help/hints or links to external learning sources.
                You may use the given context if required: \n{context}"""
            ),
            ("human", "{question}")
        ])
        llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-001', 
            temperature=0.5 
        )
        chain = prompt_template | llm
  
        response = chain.invoke({
            "question": question,
            "context": relevant_docs,
            "correct_option": correct_option
        })

        return response.text()

