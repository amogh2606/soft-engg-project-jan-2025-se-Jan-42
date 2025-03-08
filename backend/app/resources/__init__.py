from flask_restful import Api
from app.resources.auth import Login, Logout
from app.resources.users import UserResource, UsersResource
from app.resources.courses import CourseResource, AllCourses, CourseEnrollment
from app.resources.videos import VideoResource, AllVideos, RateVideo
from app.resources.assignments import AssignmentResource
from app.resources.chats import ChatSession, UserChats, AllChats
from app.resources.feedback import FeedbackResource
from app.ai_agent.chatbot_service import ChatbotService
from app.ai_agent.document_manager import KnowledgeStack
from app.ai_agent.faqs import GenerateFAQs
from app.ai_agent.video_features import VideoSummary, GenerateQuiz
from app.ai_agent.assignment_help import AssignmentHelp



api = Api(prefix='/api')


# api endpoints for authentication
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

# api endpoints for user
api.add_resource(UserResource, '/user', '/user/<int:user_id>')
api.add_resource(UsersResource, '/users')

# api endpoints for courses
api.add_resource(CourseResource, '/courses', '/courses/<int:course_id>')
api.add_resource(CourseEnrollment, '/courses/enroll', '/enrollments/<int:course_id>')
api.add_resource(AllCourses, '/courses/all')

# api endpoints for videos
api.add_resource(VideoResource, '/videos', '/videos/<int:video_id>')
api.add_resource(RateVideo, '/videos/<int:video_id>/rate')
api.add_resource(VideoSummary, '/videos/<int:video_id>/summary')
api.add_resource(GenerateQuiz, '/videos/<int:video_id>/quiz')
api.add_resource(AllVideos, '/videos/all')

# api endpoint for assignments
api.add_resource(AssignmentResource, '/assignments/<int:assignment_id>')
api.add_resource(AssignmentHelp, '/assignments/help')

# api endpoints for chats
api.add_resource(ChatSession, '/chats', '/chats/<int:chat_id>')
api.add_resource(UserChats, '/chats/user')
api.add_resource(AllChats, '/chats/all')

# api endpoints for AI agent
api.add_resource(ChatbotService, '/chatbot')
api.add_resource(KnowledgeStack, '/documents', '/documents/<int:course_id>')

# api endpoints for feedback
api.add_resource(FeedbackResource, '/feedback/<int:course_id>')

# api endpoint for generating faqs
api.add_resource(GenerateFAQs, '/faqs')

