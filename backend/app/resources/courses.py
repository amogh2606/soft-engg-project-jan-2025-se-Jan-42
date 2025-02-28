from flask import request
from flask_restful import Resource
from flask_security import current_user, auth_required  # or login_required
from sqlalchemy.exc import IntegrityError

from backend.app import db
from backend.app.models import Course


# Assuming models are in this file

class CourseResource(Resource):
    @auth_required()
    def get(self, course_id):
        """Get course details"""
        course = Course.query.get_or_404(course_id)
        
        # Check if user has access (enrolled or admin)
        if (current_user not in course.users and 
            not current_user.has_role('admin')):
            return {'message': 'Unauthorized'}, 403

        return {
            'id': course.id,
            'name': course.name,
            'description': course.description,
            'user_count': len(course.users),
            'video_count': len(course.videos),
            'assignment_count': len(course.assignments)
        }, 200

    @auth_required()
    def put(self, course_id):
        """Update course details (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        course = Course.query.get_or_404(course_id)
        data = request.get_json() or {}

        try:
            if 'name' in data:
                course.name = data['name']
            if 'description' in data:
                course.description = data['description']

            db.session.commit()
            return {'message': 'Course updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

    @auth_required()
    def delete(self, course_id):
        """Delete a course (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        course = Course.query.get_or_404(course_id)
        try:
            db.session.delete(course)  # Cascade will handle assignments
            db.session.commit()
            return {'message': 'Course deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class CourseListResource(Resource):
    @auth_required()
    def get(self):
        """Get all courses"""
        # If admin, show all courses; otherwise, show only enrolled courses
        if current_user.has_role('admin'):
            courses = Course.query.all()
        else:
            courses = current_user.courses

        return [{
            'id': course.id,
            'name': course.name,
            'description': course.description,
            'user_count': len(course.users)
        } for course in courses], 200

    @auth_required()
    def post(self):
        """Create a new course (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        data = request.get_json() or {}
        if 'name' not in data:
            return {'message': 'Course name is required'}, 400

        try:
            course = Course(
                name=data['name'],
                description=data.get('description')
            )
            db.session.add(course)
            db.session.commit()
            return {
                'message': 'Course created successfully',
                'id': course.id
            }, 201

        except IntegrityError:
            db.session.rollback()
            return {'message': 'Course name already exists'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class CourseUserListResource(Resource):
    @auth_required()
    def get(self, course_id):
        """Get all users enrolled in a course"""
        course = Course.query.get_or_404(course_id)
        
        # Check if user has access
        if (current_user not in course.users and 
            not current_user.has_role('admin')):
            return {'message': 'Unauthorized'}, 403

        return [{
            'id': user.id,
            'email': user.email
        } for user in course.users], 200

# Register the resources
def register_course_resources(api):
    api.add_resource(CourseResource, '/courses/<int:course_id>')
    api.add_resource(CourseListResource, '/courses')
    api.add_resource(CourseUserListResource, '/courses/<int:course_id>/users')

# Example usage
"""
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
register_course_resources(api)
"""
