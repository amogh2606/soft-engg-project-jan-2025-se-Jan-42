from datetime import datetime

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from backend.app import db
from backend.app.models import Course, Video, Assignment, Question
from backend.app.resources.video import is_admin




class AssignmentResource(Resource):
    @jwt_required()
    def get(self, course_id):
        assignments = Assignment.query.filter_by(course_id=course_id).all()
        return [{'id': a.id, 'week': a.week, 'due_date': a.due_date.isoformat()} for a in assignments]

    @jwt_required()
    def post(self, course_id):
        if not is_admin():
            return {'message': 'Admin access required'}, 403
        data = request.get_json()
        new_assignment = Assignment(
            course_id=course_id,
            week=data['week'],
            due_date=datetime.fromisoformat(data['due_date'])
        )
        db.session.add(new_assignment)
        db.session.commit()
        return {'message': 'Assignment created', 'id': new_assignment.id}, 201

class QuestionResource(Resource):
    @jwt_required()
    def get(self, assignment_id):
        questions = Question.query.filter_by(assignment_id=assignment_id).all()
        return [{'id': q.id, 'qno': q.qno, 'text': q.text,'option1':q.option1,'option2':q.option2,'option3':q.option3,'option4':q.option4,} for q in questions]

    @jwt_required()
    def post(self, assignment_id):
        if not is_admin():
            return {'message': 'Admin access required'}, 403
        data = request.get_json()
        new_question = Question(
            assignment_id=assignment_id,
            qno=data['qno'],
            type=data.get('type', 'MCQ'),
            text=data['text'],
            option1=data['option1'],
            option2=data['option2'],
            option3=data['option3'],
            option4=data['option4'],
            correct_option=data['correct_option']
        )
        db.session.add(new_question)
        db.session.commit()
        return {'message': 'Question added', 'id': new_question.id}, 201
