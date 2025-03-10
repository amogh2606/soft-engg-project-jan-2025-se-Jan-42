from flask_restful import Resource, reqparse, marshal_with, fields, abort
from flask_security import current_user, auth_required
from app.models import db, Chat, Message, Course

from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from app.ai_agent.embeddings import client, embedding_function


parser = reqparse.RequestParser()
parser.add_argument("chat_id", type=int, required=True)
parser.add_argument("course_id", type=int)
parser.add_argument("query", required=True)

response_fields = {
    'chat_id': fields.Integer,
    'timestamp': fields.String,
    'message': fields.String(attribute='text')
}

class ChatbotService(Resource):
    @auth_required('session')
    @marshal_with(response_fields)
    def post(self):
        args = parser.parse_args()
        chat_id = args.get('chat_id')
        chat = db.get_or_404(Chat, chat_id)
        if not (chat.active and chat.user_id == current_user.id):
            abort(404, message="Chat not found")
        
        query = args.get('query')
        course_id = args.get('course_id')
        response = self.generate_response(query, chat_id, course_id)

        # Save the question and response in db
        user_query = Message(chat_id=chat.id, text=query, is_response=False)
        ai_response = Message(chat_id=chat.id, text=response, is_response=True)
        
        db.session.add_all([user_query, ai_response])
        db.session.commit()

        return ai_response
    
    
    def generate_response(self, query, chat_id, course_id=None):
        if course_id:
            db.get_or_404(Course, course_id, description="Course not found")
            
        collection_name = f'course_{course_id}' if course_id else 'general'
        vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=embedding_function,
            client=client,
            create_collection_if_not_exists=False
        )
        retriever = vector_store.as_retriever(
            search_kwargs={'k': 4}
        )
        llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-001', 
            temperature=0.5 
        )
        prompt_template = self.create_prompt_template()
        chain = prompt_template | llm

        messages = self.load_conversation(chat_id)
        messages.append(HumanMessage(query))
        
        res = retriever.invoke(query)
        relevant_docs = '\n\n'.join(set(doc.page_content for doc in res))

        response = chain.invoke({"messages": messages, "context": relevant_docs})
        
        return response.text()
    

    def create_prompt_template(self):           
        prompt_template = ChatPromptTemplate([
            ("system", """You are a chatbot in an e-learning platform. 
                Provide a concise friendly response based on the conversation.
                You can also point to external sources of information if required.
                You may use the given context if relevant: \n\n{context}"""),

            ("placeholder", "{messages}"),
        ])
        return prompt_template
    

    def load_conversation(self, chat_id):
        db.get_or_404(Chat, chat_id, description="Chat not found")
        previous_msgs = db.session.scalars(db.select(Message)
            .filter_by(chat_id=chat_id)
            .order_by(Message.timestamp.desc())
            .limit(10)
        ).all()
        messages = []
        for msg in reversed(previous_msgs):
            if msg.is_response:
                messages.append(AIMessage(msg.text))
            else:
                messages.append(HumanMessage(msg.text))
        
        return messages

