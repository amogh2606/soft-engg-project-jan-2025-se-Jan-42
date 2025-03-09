import io, csv
from flask_restful import Resource, reqparse, marshal_with, fields, abort, marshal
from flask_security import current_user, roles_accepted, auth_required
from flask import request, send_file
from app.models import db, Chat, Message



# Response fields for chat session
chat_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'created': fields.String,
    'active': fields.Boolean,
    'bookmarked': fields.Boolean,
    'messages': fields.List(fields.Nested({
        'id': fields.Integer,
        'text': fields.String,
        'timestamp': fields.String,
        'is_response': fields.Boolean
    }))
}

class ChatSession(Resource):
    # Load chat session
    @auth_required('session')
    @marshal_with(chat_fields)
    def get(self, chat_id=None):
        if chat_id:
            # get any specific chat session
            chat = db.get_or_404(Chat, chat_id, description="Chat not found")
            if not (chat.user_id == current_user.id or current_user.has_role('admin')):
                abort(404, message="Chat not found")
        else:
            # get the active chat session
            stmt = db.select(Chat).filter_by(user_id=current_user.id, active=True)
            chat = db.session.scalar(stmt)
            if not chat:
                return self.post()
        
        return chat
    

    # Create new chat session
    @auth_required('session')
    @marshal_with(chat_fields)
    def post(self):
        stmt = db.select(Chat).filter_by(user_id=current_user.id, active=True)
        active_sessions = db.session.scalars(stmt)
        if active_sessions:
            for session in active_sessions:
                session.active = False

        new_chat = Chat(user_id=current_user.id)
        db.session.add(new_chat)
        db.session.commit()

        return new_chat
    

    # Bookmark or rename chat
    @auth_required('session')
    @marshal_with(chat_fields)
    def put(self, chat_id):
        chat = db.session.get(Chat, chat_id)
        if not chat or chat.user_id != current_user.id:
            abort(404, message="Chat not found")
        
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('title')
        parser.add_argument('bookmarked', type=bool)

        args = parser.parse_args()
        title = args.get('title')
        bookmarked = args.get('bookmarked')

        if title:
            chat.title = title
        if bookmarked is not None:
            chat.bookmarked = bookmarked

        db.session.commit()
        return chat
    

    # Delete a chat session
    @roles_accepted('admin')
    def delete(self, chat_id):
        chat = db.get_or_404(Chat, chat_id, description="Chat not found")
        db.session.delete(chat)
        db.session.commit()
        
        return {"message": "Chat deleted successfully"}


# Response fields for chat list
chat_list_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'created': fields.String,
    'active': fields.Boolean,
    'bookmarked': fields.Boolean,
}


class UserChats(Resource):
    # Get chat history for current user
    @auth_required('session')
    @marshal_with(chat_list_fields)
    def get(self):
        stmt = db.select(Chat).filter_by(user_id=current_user.id)
        chats = db.session.scalars(stmt).all()
        return chats


class AllChats(Resource):
    # Get entire chat history
    @roles_accepted('admin')
    def get(self):
        if request.args.get('export') in ('true', '1'):
            return self.export_chats()
        
        chats = db.session.scalars(db.select(Chat)).all() 
        return marshal(chats, chat_list_fields)


    # Export chats as CSV
    def export_chats(self):
        all_chats = db.session.scalars(db.select(Message)).all()
        
        # Create StringIO first to write content
        output_text = io.StringIO()
        writer = csv.writer(output_text)
        writer.writerow(['msg_id', 'chat_id', 'message', 'timestamp', 'sender']) # header row

        for msg in all_chats:
            if msg.is_response:
                writer.writerow([msg.id, msg.chat_id, msg.text, msg.timestamp, 'AI'])
            else:
                writer.writerow([msg.id, msg.chat_id, msg.text, msg.timestamp, 'User'])

        # Convert to BytesIO for send_file
        output_bytes = io.BytesIO()
        output_bytes.write(output_text.getvalue().encode('utf-8'))
        output_bytes.seek(0)

        return send_file(output_bytes, mimetype='text/csv', download_name='chats.csv', as_attachment=True)
