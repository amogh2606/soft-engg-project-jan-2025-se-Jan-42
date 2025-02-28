from sqlite3 import IntegrityError

from flask_jwt_extended import current_user
from flask_restful import Resource
from flask_security import auth_required

from backend.app.models import UserCourses, User, Course, db


class UserCourseResource(Resource):
    @auth_required()
    def get(self, user_id, course_id):
        """Check if a specific user-course association exists"""
        # Allow users to check their own courses or admin to check any
        if current_user.id != user_id and not current_user.has_role('admin'):
            return {'message': 'Unauthorized'}, 403

        association = UserCourses.query.filter_by(
            user_id=user_id,
            course_id=course_id
        ).first()

        if not association:
            return {'message': 'Association not found'}, 404

        return {
            'user_id': association.user_id,
            'course_id': association.course_id
        }, 200

    @auth_required()
    def post(self, user_id, course_id):
        """Add a course to a user"""
        # Allow users to enroll themselves or admin to enroll anyone
        if current_user.id != user_id and not current_user.has_role('admin'):
            return {'message': 'Unauthorized'}, 403

        # Verify user and course exist
        user = User.query.get_or_404(user_id)
        course = Course.query.get_or_404(course_id)

        try:
            association = UserCourses(
                user_id=user_id,
                course_id=course_id
            )
            db.session.add(association)
            db.session.commit()
            return {
                'message': 'Course enrolled successfully',
                'user_id': user_id,
                'course_id': course_id
            }, 201

        except IntegrityError:
            db.session.rollback()
            return {'message': 'User is already enrolled in this course'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

    @auth_required()
    def delete(self, user_id, course_id):
        """Remove a course from a user"""
        # Allow users to unenroll themselves or admin to unenroll anyone
        if current_user.id != user_id and not current_user.has_role('admin'):
            return {'message': 'Unauthorized'}, 403

        association = UserCourses.query.filter_by(
            user_id=user_id,
            course_id=course_id
        ).first_or_404()

        try:
            db.session.delete(association)
            db.session.commit()
            return {'message': 'Course unenrolled successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class UserCourseListResource(Resource):
    @auth_required()
    def get(self, user_id):
        """Get all courses for a specific user"""
        # Allow users to see their own courses or admin to see anyone's
        if current_user.id != user_id and not current_user.has_role('admin'):
            return {'message': 'Unauthorized'}, 403

        user = User.query.get_or_404(user_id)
        courses = [{
            'course_id': uc.course_id
            # Add more course details if needed by joining with Course table
        } for uc in user.courses]

        return {
            'user_id': user_id,
            'courses': courses,
            'count': len(courses)
        }, 200
