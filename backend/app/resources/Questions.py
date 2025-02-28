from flask import request
from flask_restful import Resource
from flask_security import current_user, auth_required  # or login_required
from sqlalchemy.exc import IntegrityError

from backend.app import db
from backend.app.models import Question, Assignment


class QuestionResource(Resource):
    @auth_required()
    def get(self, question_id):
        """Get question details"""
        question = Question.query.get_or_404(question_id)

        # Check if user has access (enrolled in course or admin)
        if (current_user not in question.assignment.course.users and
            not current_user.has_role('admin')):
            return {'message': 'Unauthorized'}, 403

        return {
            'id': question.id,
            'assignment_id': question.assignment_id,
            'qno': question.qno,
            'type': question.type,
            'text': question.text,
            'options': [
                question.option1,
                question.option2,
                question.option3,
                question.option4
            ],
            'correct_option': question.correct_option
        }, 200

    @auth_required()
    def put(self, question_id):
        """Update question details (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        question = Question.query.get_or_404(question_id)
        data = request.get_json() or {}

        try:
            if 'qno' in data:
                question.qno = data['qno']
            if 'type' in data:
                question.type = data['type']
            if 'text' in data:
                question.text = data['text']
            if 'option1' in data:
                question.option1 = data['option1']
            if 'option2' in data:
                question.option2 = data['option2']
            if 'option3' in data:
                question.option3 = data['option3']
            if 'option4' in data:
                question.option4 = data['option4']
            if 'correct_option' in data:
                question.correct_option = data['correct_option']
            if 'assignment_id' in data:
                # Verify new assignment exists
                Assignment.query.get_or_404(data['assignment_id'])
                question.assignment_id = data['assignment_id']

            db.session.commit()
            return {'message': 'Question updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

    @auth_required()
    def delete(self, question_id):
        """Delete a question (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        question = Question.query.get_or_404(question_id)
        try:
            db.session.delete(question)
            db.session.commit()
            return {'message': 'Question deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class QuestionListResource(Resource):
    @auth_required()
    def get(self, assignment_id=None):
        """Get all questions, optionally filtered by assignment"""
        if assignment_id:
            assignment = Assignment.query.get_or_404(assignment_id)
            # Check if user has access
            if (current_user not in assignment.course.users and
                not current_user.has_role('admin')):
                return {'message': 'Unauthorized'}, 403
            questions = Question.query.filter_by(assignment_id=assignment_id).order_by(Question.qno).all()
        else:
            # Admin sees all questions, users see only their courses' questions
            if current_user.has_role('admin'):
                questions = Question.query.all()
            else:
                questions = [question for course in current_user.courses
                           for assignment in course.assignments
                           for question in assignment.questions]

        return [{
            'id': question.id,
            'assignment_id': question.assignment_id,
            'qno': question.qno,
            'type': question.type,
            'text': question.text,
            'options': [
                question.option1,
                question.option2,
                question.option3,
                question.option4
            ],
            'correct_option': question.correct_option
        } for question in questions], 200

    @auth_required()
    def post(self):
        """Create a new question (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        data = request.get_json() or {}
        required_fields = ['assignment_id', 'qno', 'text', 'option1', 'option2',
                         'option3', 'option4', 'correct_option']
        if not all(field in data for field in required_fields):
            return {'message': 'Missing required fields'}, 400

        try:
            # Verify assignment exists
            Assignment.query.get_or_404(data['assignment_id'])

            question = Question(
                assignment_id=data['assignment_id'],
                qno=data['qno'],
                type=data.get('type', 'MCQ'),
                text=data['text'],
                option1=data['option1'],
                option2=data['option2'],
                option3=data['option3'],
                option4=data['option4'],
                correct_option=data['correct_option']
            )
            db.session.add(question)
            db.session.commit()
            return {
                'message': 'Question created successfully',
                'id': question.id
            }, 201

        except IntegrityError:
            db.session.rollback()
            return {'message': 'Question creation failed - possible duplicate'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

# Register the resources
def register_question_resources(api):
    api.add_resource(QuestionResource, '/questions/<int:question_id>')
    api.add_resource(QuestionListResource,
                    '/questions',  # All questions
                    '/assignments/<int:assignment_id>/questions'  # Questions for specific assignment
                    )

# Example usage
"""
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
register_question_resources(api)
"""
