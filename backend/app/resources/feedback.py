from flask_restful import Resource, reqparse, marshal_with, fields, abort
from flask_security import roles_required, current_user
from app.models import db, Feedback, Course



feedback_fields = {
    'id': fields.Integer,
    'course_id': fields.Integer,
    'created': fields.DateTime('iso8601'),
    'title': fields.String,
    'text': fields.String
}

class FeedbackResource(Resource):
    # Get feedback for a specific course
    @roles_required('instructor')
    @marshal_with(feedback_fields)
    def get(self, course_id):
        course = db.get_or_404(Course, course_id, description="Course not found")
        if course not in current_user.courses:
            abort(400, message="Course not enrolled")
        
        stmt = db.select(Feedback).filter_by(course_id=course_id)
        feedbacks = db.session.scalars(stmt)

        return feedbacks


    # Post feedback for a specific course
    @roles_required('student')
    def post(self, course_id):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('title', type=str, required=True, nullable=False)
        parser.add_argument('text', type=str)

        args = parser.parse_args()
        title = args.get('title')
        text = args.get('text')

        course = db.get_or_404(Course, course_id, description="Course not found")
        if course not in current_user.courses:
            abort(400, message="Course not enrolled")

        new_feedback = Feedback(course_id=course_id, title=title, text=text)
        db.session.add(new_feedback)
        db.session.commit()

        return {"message": "Feedback submitted successfully"}, 201
    
