from flask_restful import Resource, reqparse, abort
from flask_security import current_user, login_user, logout_user
from app.security import security



parser = reqparse.RequestParser()
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)


class Login(Resource):
    def post(self):
        if current_user.is_authenticated:
            abort(400, message="Already logged in")
        
        args = parser.parse_args()
        email = args.get('email')
        password = args.get('password')

        user = security.datastore.find_user(email=email)
        if user and user.verify_and_update_password(password):
            if user.has_role('instructor') and not user.courses:
                abort(400, message="No courses have been assigned to you yet")
                
            if login_user(user):
                return {"message": "Logged in successfully"}
            else:
                abort(401, message="User not active")
        
        abort(401, message="Invalid credentials")


class Logout(Resource):
    def post(self):
        logout_user()        
        return {"message": "Logged out successfully"}

