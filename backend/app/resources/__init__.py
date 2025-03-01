from flask_restful import Api

from .assignment_and_question import AssignmentResource, QuestionResource
from .chats import ChatSession, UserChats, AllChats
from .courses import CourseResource, AssignCourseResource, DeassignCourseResource
from .user_and_course import CourseUsersResource, UserCoursesResource
from .users import UserResource, LoginResource, AdminUserCreation, InstructorUserCreation
from .video import CourseVideosResource, VideoResource

api = Api(prefix='/api')


# api endpoints for chats
api.add_resource(ChatSession, '/chat', '/chat/<int:chat_id>')
api.add_resource(UserChats, '/user/chats')
api.add_resource(AllChats, '/admin/chats')

# Users
api.add_resource(UserResource, '/users', '/users/<int:user_id>')
api.add_resource(LoginResource, '/login')
api.add_resource(AdminUserCreation, '/admin/create')
api.add_resource(InstructorUserCreation, '/instructor/create')


#Courses
api.add_resource(CourseResource, '/course', '/course/<int:course_id>')
api.add_resource(AssignCourseResource, '/assign_course')
api.add_resource(DeassignCourseResource, '/deassign_course')

api.add_resource(UserCoursesResource, '/user/<int:user_id>/courses')
api.add_resource(CourseUsersResource, '/course/<int:course_id>/users')

#video
api.add_resource(CourseVideosResource, '/courses/<int:course_id>/videos')

api.add_resource(VideoResource, '/videos', '/videos/<int:video_id>')

api.add_resource(AssignmentResource, '/courses/<int:course_id>/assignments')
api.add_resource(QuestionResource, '/assignments/<int:assignment_id>/questions')

