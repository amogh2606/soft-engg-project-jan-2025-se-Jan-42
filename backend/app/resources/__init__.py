from flask_restful import Api

from .Assignment import AssignmentListResource, AssignmentResource
from .Questions import QuestionResource, QuestionListResource
from .chats import ChatSession, UserChats, AllChats
from .courses import CourseResource, CourseListResource, CourseUserListResource
from .user_courses import UserCourseResource, UserCourseListResource
from .users import UserResource, UserListResource
from .videos import VideoResource, VideoListResource

api = Api(prefix='/api')


# api endpoints for chats
api.add_resource(ChatSession, '/chat', '/chat/<int:chat_id>')

api.add_resource(UserChats, '/user/chats')

api.add_resource(AllChats, '/admin/chats')

api.add_resource(AssignmentResource, '/assignments/<int:assignment_id>')
api.add_resource(AssignmentListResource,
                    '/assignments',  # All assignments
                    '/courses/<int:course_id>/assignments'  # Assignments for specific course
                    )

api.add_resource(CourseResource, '/courses/<int:course_id>')
api.add_resource(CourseListResource, '/courses')
api.add_resource(CourseUserListResource, '/courses/<int:course_id>/users')

api.add_resource(QuestionResource, '/questions/<int:question_id>')
api.add_resource(QuestionListResource,
                    '/questions',  # All questions
                    '/assignments/<int:assignment_id>/questions'  # Questions for specific assignment
                    )
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserListResource, '/users')

api.add_resource(UserCourseResource, '/users/<int:user_id>/courses/<int:course_id>')
api.add_resource(UserCourseListResource, '/users/<int:user_id>/courses')

api.add_resource(VideoResource, '/videos/<int:video_id>')
api.add_resource(VideoListResource,
                    '/videos',  # All videos
                    '/courses/<int:course_id>/videos'  # Videos for specific course
                    )

