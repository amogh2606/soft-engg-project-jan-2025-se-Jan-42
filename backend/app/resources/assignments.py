from flask_restful import Resource, reqparse, marshal_with, fields, inputs, abort
from flask_security import roles_required, auth_required, current_user
from app.models import db, Assignment, Course



question_fields = {
    'id': fields.Integer,
    'qno': fields.Integer,
    'type': fields.String,
    'text': fields.String,
    'option_1': fields.String,
    'option_2': fields.String,
    'option_3': fields.String,
    'option_4': fields.String,
    'correct_option': fields.Integer
}

assignment_fields = {
    'id': fields.Integer,
    'course_id': fields.Integer,
    'week': fields.Integer,
    'due_date': fields.String,
    'questions': fields.List(fields.Nested(question_fields))
}

class AssignmentResource(Resource):
    @auth_required('session')
    @marshal_with(assignment_fields)
    def get(self, assignment_id):
        assignment = db.get_or_404(Assignment, assignment_id, description='Assignment not found')
        if not current_user.has_role('admin'):
            if assignment.course not in current_user.courses:
                abort(400, message="Course not enrolled")
        
        return assignment


    @roles_required('admin')
    def put(self, assignment_id):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('course_id', type=int)
        parser.add_argument('week', type=int, choices=range(1, 13))
        parser.add_argument('due_date', type=inputs.datetime_from_iso8601, help="Use ISO format for due_date")

        assignment = db.get_or_404(Assignment, assignment_id, description="Assignment not found")

        args = parser.parse_args()
        course_id = args.get('course_id')
        week = args.get('week')
        due_date = args.get('due_date')

        if course_id:
            db.get_or_404(Course, course_id, description='Course not found')
            assignment.course_id = course_id

        if week: assignment.week = week
        if due_date: assignment.due_date = due_date

        db.session.commit()
        return {"message": "Updated successfully"}


    @roles_required('admin')
    def delete(self, assignment_id):
        assignment = db.get_or_404(Assignment, assignment_id, description="Assignment not found")
        db.session.delete(assignment)
        db.session.commit()

        return {"message": "Deleted successfully"}


