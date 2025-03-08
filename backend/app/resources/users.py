from flask_restful import Resource, reqparse, fields, marshal_with, abort
from flask_security import hash_password, roles_required, auth_required, current_user
from app.security import security
from app.models import db, User
import re



user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'name': fields.String,
    'roles': fields.List(fields.String(attribute='name')),
    'courses': fields.List(fields.Nested({
        'id': fields.Integer,
        'name': fields.String
    }))
}


class UserResource(Resource):
    # get user details
    @auth_required('session')
    @marshal_with(user_fields)
    def get(self):
        return current_user
    

    # user registration
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, nullable=False, trim=True)
        parser.add_argument('password', required=True, nullable=False)
        parser.add_argument('name', required=True, nullable=False, trim=True)
        
        args = parser.parse_args()
        email = args.get('email').lower()
        password = args.get('password')
        name = args.get('name')

        self.validate_email(email)
        if len(password) < 6:
            abort(400, message="Mininmum password length is 6 characters")
        
        roles = ['instructor'] if current_user.has_role('admin') else ['student']
        
        security.datastore.create_user(
            email=email, 
            password=hash_password(password), 
            name=name, 
            roles=roles
        )

        db.session.commit()
        return {"message": "Registered successfully"}, 201


    # update user details
    @auth_required('session')
    def put(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('email', nullable=False)
        parser.add_argument('name', nullable=False)

        args = parser.parse_args()
        email = args.get('email').lower()
        name = args.get('name')

        if email:
            self.validate_email(email)
            current_user.email = email
        if name:
            current_user.name = name

        db.session.commit()
        return {"message": "Updated successfully"}


    # delete a user
    @roles_required('admin')
    def delete(self, user_id):
        user = db.session.get(User, user_id)
        if not user:
            abort(400, description="User not found")
            
        security.datastore.delete_user(user)
        db.session.commit()

        return {"message": "Deleted successfully"}


    # email validator
    def validate_email(self, email):      
        pattern = r'^\w[\w\.-]*@\w[\w\.-]*\.\w+$'
        if not re.fullmatch(pattern, email):
            abort(400, message="Invalid email address")
    
        if security.datastore.find_user(email=email):
            abort(400, message="Email already exists")
            
