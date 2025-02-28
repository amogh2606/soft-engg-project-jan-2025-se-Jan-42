from sqlite3 import IntegrityError

from fastapi.utils import generate_unique_id
from flask import request
from flask_jwt_extended import current_user
from flask_restful import Resource
from flask_security import auth_required
from flask_security.utils import hash_password

from backend.app import db
from backend.app.models import User, UserCourses, Course




class UserResource(Resource):
   # @auth_required() # or @login_required
    def get(self, user_id=None):
        """Get user details by ID or current user if no ID provided"""
        if user_id:
            user = User.query.get_or_404(user_id)
            # Check if current user has permission to view this user
            if current_user.id != user.id and not current_user.has_role('admin'):
                return {'message': 'Unauthorized'}, 403
        else:
            user = current_user

        return {
            'id': user.id,
            'email': user.email,
            'active': user.active,
            'roles': [role.name for role in user.roles],
            'courses': [course.id for course in user.courses]
        }, 200

    @auth_required()
    def put(self, user_id):
        """Update user details"""
        # Only admin or the user themselves can update
        if current_user.id != user_id and not current_user.has_role('admin'):
            return {'message': 'Unauthorized'}, 403

        user = User.query.get_or_404(user_id)
        data = request.get_json() or {}

        try:
            if 'email' in data:
                user.email = data['email']
            if 'active' in data and current_user.has_role('admin'):
                user.active = data['active']
            if 'password' in data:
                user.password = hash_password(data['password']) # You'll need to implement password hashing

            db.session.commit()
            return {'message': 'User updated successfully'}, 200

        except IntegrityError:
            db.session.rollback()
            return {'message': 'Email already exists'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

    @auth_required()
    def delete(self, user_id):
        """Delete a user (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        user = User.query.get_or_404(user_id)
        try:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
#
class UserListResource(Resource):
    @auth_required()
    def get(self):
        """Get list of all users (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        users = User.query.all()
        return [{
            'id': user.id,
            'email': user.email,
            'active': user.active,
            'roles': [role.name for role in user.roles]
        } for user in users], 200

    @auth_required()
    def post(self):
        """Create a new user (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        data = request.get_json() or {}

        required_fields = ['email', 'password']
        if not all(field in data for field in required_fields):
            return {'message': 'Missing required fields'}, 400

        try:
            user = User(
                email=data['email'],
                password=hash_password(data['password']), # Implement password hashing
                fs_uniquifier=generate_unique_id() # Implement unique ID generation
            )
            db.session.add(user)
            db.session.commit()
            return {'message': 'User created successfully', 'id': user.id}, 201

        except IntegrityError:
            db.session.rollback()
            return {'message': 'Email already exists'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500


