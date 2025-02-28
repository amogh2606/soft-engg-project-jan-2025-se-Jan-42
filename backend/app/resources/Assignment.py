from flask import request
from flask_restful import Resource
from flask_security import current_user, auth_required  # or login_required
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from backend.app.models import Assignment, Course, db


class AssignmentResource(Resource):
    @auth_required()
    def get(self, assignment_id):
        """Get assignment details"""
        assignment = Assignment.query.get_or_404(assignment_id)

        # Check if user has access (enrolled in course or admin)
        if (current_user not in assignment.course.users and
            not current_user.has_role('admin')):
            return {'message': 'Unauthorized'}, 403

        return {
            'id': assignment.id,
            'course_id': assignment.course_id,
            'week': assignment.week,
            'due_date': assignment.due_date.isoformat(),
            'question_count': len(assignment.questions)
        }, 200

    @auth_required()
    def put(self, assignment_id):
        """Update assignment details (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        assignment = Assignment.query.get_or_404(assignment_id)
        data = request.get_json() or {}

        try:
            if 'week' in data:
                assignment.week = data['week']
            if 'due_date' in data:
                assignment.due_date = datetime.fromisoformat(data['due_date'])
            if 'course_id' in data:
                # Verify new course exists
                Course.query.get_or_404(data['course_id'])
                assignment.course_id = data['course_id']

            db.session.commit()
            return {'message': 'Assignment updated successfully'}, 200

        except ValueError as e:
            return {'message': 'Invalid date format'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

    @auth_required()
    def delete(self, assignment_id):
        """Delete an assignment (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        assignment = Assignment.query.get_or_404(assignment_id)
        try:
            db.session.delete(assignment)
            db.session.commit()
            return {'message': 'Assignment deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class AssignmentListResource(Resource):
    @auth_required()
    def get(self, course_id=None):
        """Get all assignments, optionally filtered by course"""
        if course_id:
            course = Course.query.get_or_404(course_id)
            # Check if user has access
            if (current_user not in course.users and
                not current_user.has_role('admin')):
                return {'message': 'Unauthorized'}, 403
            assignments = Assignment.query.filter_by(course_id=course_id).all()
        else:
            # Admin sees all assignments, users see only their courses' assignments
            if current_user.has_role('admin'):
                assignments = Assignment.query.all()
            else:
                assignments = [assignment for course in current_user.courses
                             for assignment in course.assignments]

        return [{
            'id': assignment.id,
            'course_id': assignment.course_id,
            'week': assignment.week,
            'due_date': assignment.due_date.isoformat(),
            'question_count': len(assignment.questions)
        } for assignment in assignments], 200

    @auth_required()
    def post(self):
        """Create a new assignment (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        data = request.get_json() or {}
        required_fields = ['course_id', 'week', 'due_date']
        if not all(field in data for field in required_fields):
            return {'message': 'Missing required fields'}, 400

        try:
            # Verify course exists
            Course.query.get_or_404(data['course_id'])

            assignment = Assignment(
                course_id=data['course_id'],
                week=data['week'],
                due_date=datetime.fromisoformat(data['due_date'])
            )
            db.session.add(assignment)
            db.session.commit()
            return {
                'message': 'Assignment created successfully',
                'id': assignment.id
            }, 201

        except ValueError as e:
            return {'message': 'Invalid date format'}, 400
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Assignment creation failed'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

# Register the resources
def register_assignment_resources(api):
    api.add_resource(AssignmentResource, '/assignments/<int:assignment_id>')
    api.add_resource(AssignmentListResource,
                    '/assignments',  # All assignments
                    '/courses/<int:course_id>/assignments'  # Assignments for specific course
                    )

