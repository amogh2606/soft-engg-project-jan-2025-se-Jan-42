import os
from getpass import getpass

# check if LLM API key is set
if 'GOOGLE_API_KEY' not in os.environ:
    os.environ['GOOGLE_API_KEY'] = getpass("Enter the Google API key: ")


from flask_restful import Api
from app.resources.chats import ChatSession, UserChats, AllChats
from app.ai_agent.chatbot_service import ChatbotService
from app.ai_agent.document_manager import KnowledgeStack


api = Api(prefix='/api')


# api endpoints for chats
api.add_resource(ChatSession, '/chats/active', '/chats/<int:chat_id>')
api.add_resource(UserChats, '/chats/user')
api.add_resource(AllChats, '/chats/all')

# api endpoints for AI agent
api.add_resource(ChatbotService, '/chatbot')
api.add_resource(KnowledgeStack, '/documents', '/documents/<int:course_id>')

