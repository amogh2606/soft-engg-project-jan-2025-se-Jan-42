from flask_restful import Resource, reqparse, marshal_with, fields, abort
from flask_security import roles_accepted, auth_required, current_user
from app.models import db, Course, User



course_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'videos': fields.List(fields.Nested({
        'id': fields.Integer,
        'title': fields.String,
        'week': fields.Integer,
        'lecture': fields.Integer
    })),
    'assignments': fields.List(fields.Nested({
        'id': fields.Integer,
        'week': fields.String,
    }))
}

class CourseResource(Resource):
    # Get a specific course
    @auth_required('session')
    @marshal_with(course_fields)
    def get(self, course_id):
        course = db.get_or_404(Course, course_id, description='Course not found')

        if not current_user.has_role('admin'):
            if course not in current_user.courses:
                abort(400, message="Course not enrolled")

        return course


    # Create a new course
    @roles_accepted('admin')
    @marshal_with(course_fields)
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('name', required=True, nullable=False)
        parser.add_argument('description')

        args = parser.parse_args()
        name = args.get('name').lower()
        description = args.get('description')

        stmt = db.select(Course).filter_by(name=name)
        if db.session.scalar(stmt):
            abort(400, message="Course already exists")

        new_course = Course(name=name, description=description)  
        db.session.add(new_course)
        db.session.commit()

        return {"Course created successfully"}, 201


    # Update a specific course
    @roles_accepted('admin')
    def put(self, course_id):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('name')
        parser.add_argument('description')

        course = db.get_or_404(Course, course_id, description="Course not found")
        
        args = parser.parse_args()
        name = args.get('name')
        description = args.get('description')

        if name:
            name = name.lower()
            stmt = db.select(Course).filter_by(name=name)
            if db.session.scalar(stmt):
                abort(400, message="Course name already exists")
            else:
                course.name = name
        
        if description:
            course.description = description
        
        db.session.commit()
        return {"message": "Updated successfully"}


    # Delete a specific course
    @roles_accepted('admin')
    def delete(self, course_id):
        course = db.get_or_404(Course, course_id, description="Course not found")
        db.session.delete(course)
        db.session.commit()

        return {"message": "Deleted successfully"}


course_list_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class AllCourses(Resource):
    # Get all courses
    @roles_accepted('admin','student')
    @marshal_with(course_list_fields)
    def get(self):
        all_courses = db.session.scalars(db.select(Course)).all()
        return all_courses


class CourseEnrollment(Resource):
    # Enroll a user to a course
    @roles_accepted('student', 'admin')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('course_id', type=int, required=True, nullable=False)
        parser.add_argument('user_id', type=int, required=True, nullable=False)

        args = parser.parse_args()
        course_id = args.get('course_id')
        user_id = args.get('user_id')

        # check if student is enrolling themselves
        if current_user.has_role('student') and current_user.id != user_id:
            abort(403)

        course = db.get_or_404(Course, course_id, description="Course not found")
        user = db.get_or_404(User, user_id, description="User not found")
        if course in user.courses:
            abort(400, message="User already enrolled")

        course.users.append(user)
        db.session.commit()

        return {"message": "Enrolled successfully"}, 201

