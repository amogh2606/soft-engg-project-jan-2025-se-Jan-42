import io, csv
from flask_restful import Resource, marshal_with, fields, abort
from flask_security import current_user, roles_accepted, auth_required
from flask import request, send_file
from app.models import db, Chat, Message



# Response fields for chat session
chat_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'created': fields.DateTime('iso8601'),
    'active': fields.Boolean,
    'bookmarked': fields.Boolean,
    'messages': fields.List(fields.Nested({
        'id': fields.Integer,
        'text': fields.String,
        'timestamp': fields.DateTime('iso8601'),
        'is_response': fields.Boolean
    }))
}

class ChatSession(Resource):
    # Load chat session
    @auth_required()
    @marshal_with(chat_fields)
    def get(self, chat_id=None):
        if chat_id:
            # get any specific chat session
            chat = db.get_or_404(Chat, chat_id)
            if not (chat.user_id == current_user.id or current_user.has_role('admin')):
                abort(404, message="Chat not found")
        else:
            # get the active chat session
            if current_user.has_role('admin'):
                abort(404)
            stmt = db.select(Chat).filter_by(user_id=current_user.id, active=True)
            chat = db.session.scalar(stmt)
            if not chat:
                return self.post()
        
        return chat
    

    # Create new chat session
    @roles_accepted('student', 'instructor')
    @marshal_with(chat_fields)
    def post(self):
        stmt = db.select(Chat).filter_by(user_id=current_user.id, active=True)
        active_sessions = db.session.scalars(stmt)
        if active_sessions:
            for session in active_sessions:
                session.active = False
            db.session.commit()

        new_session = Chat(user_id=current_user.id)
        db.session.add(new_session)
        db.session.commit()
        return new_session


# Response fields for chat list
chat_list_fields = chat_fields.copy()
chat_list_fields.pop('messages')


class UserChats(Resource):
    # Get chat history for current user
    @roles_accepted('student', 'instructor')
    @marshal_with(chat_list_fields)
    def get(self):
        stmt = db.select(Chat).filter_by(user_id=current_user.id)
        return db.session.scalars(stmt)


class AllChats(Resource):
    # Get entire chat history
    @roles_accepted('admin')
    @marshal_with(chat_list_fields)
    def get(self):
        if request.args.get('export') in ('true', '1'):
            return self.export_chats()
        
        return db.session.scalars(db.select(Chat))


    # Export chats as CSV
    @roles_accepted('admin')
    def export_chats(self):
        all_chats = db.session.scalars(db.select(Message))
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['id', 'chat_id', 'text', 'timestamp', 'is_response']) # header row

        for msg in all_chats:
            writer.writerow([msg.id, msg.chat_id, msg.text, msg.timestamp, msg.is_response])

        output.seek(0)

        return send_file(output, mimetype='text/csv', attachment_filename='chats.csv', as_attachment=True)
