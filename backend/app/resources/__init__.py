from flask_restful import Api
from app.resources.auth import Login, Logout
from app.resources.users import UserResource
from app.resources.courses import CourseResource, AllCourses
from app.resources.videos import VideoResource, AllVideos, RateVideo
from app.resources.chats import ChatSession, UserChats, AllChats
from app.resources.faqs import GenerateFAQs
from app.ai_agent.chatbot_service import ChatbotService
from app.ai_agent.document_manager import KnowledgeStack



api = Api(prefix='/api')


# api endpoints for authentication
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

# api endpoints for user
api.add_resource(UserResource, '/user', '/user/<int:user_id>')

# api endpoints for courses
api.add_resource(CourseResource, '/courses' '/courses/<int:course_id>')
api.add_resource(AllCourses, '/courses/all')

# api endpoints for videos
api.add_resource(VideoResource, '/videos', '/videos/<int:video_id>')
api.add_resource(RateVideo, '/videos/<int:video_id>/rate')
api.add_resource(AllVideos, '/videos/all')

# api endpoints for chats
api.add_resource(ChatSession, '/chats/active', '/chats/<int:chat_id>')
api.add_resource(UserChats, '/chats/user')
api.add_resource(AllChats, '/chats/all')

# api endpoints for AI agent
api.add_resource(ChatbotService, '/chatbot')
api.add_resource(KnowledgeStack, '/documents', '/documents/<int:course_id>')

# api endpoint for generating faqs
api.add_resource(GenerateFAQs, '/faqs')

