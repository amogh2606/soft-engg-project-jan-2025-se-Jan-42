from flask_restful import Api
from .chats import ChatSession, UserChats, AllChats



api = Api(prefix='/api')


# api endpoints for chats
api.add_resource(ChatSession, '/chat', '/chat/<int:chat_id>')
api.add_resource(UserChats, '/user/chats')
api.add_resource(AllChats, '/admin/chats')

