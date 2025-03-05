from flask_restful import Resource, reqparse, marshal_with, fields, abort
from flask_security import roles_required, auth_required, current_user
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
    @roles_required('admin')
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
    @roles_required('admin')
    def put(self, course_id):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('name')
        parser.add_argument('description')
        parser.add_argument('user_id', type=int)

        course = db.get_or_404(Course, course_id, description="Course not found")
        
        args = parser.parse_args()
        name = args.get('name')
        description = args.get('description')
        user_id = args.get('user_id')

        if name:
            name = name.lower()
            stmt = db.select(Course).filter_by(name=name)
            if db.session.scalar(stmt):
                abort(400, message="Course already exists")
            else:
                course.name = name
        
        if description:
            course.description = description
        
        # enroll user to course
        if user_id:
            user = db.get_or_404(User, user_id, description="User not found")
            if user in course.users:
                abort(400, message="User already enrolled")
            
            course.users.append(user)

        db.session.commit()
        return {"message": "Updated successfully"}


    # Delete a specific course
    @roles_required('admin')
    def delete(self, course_id):
        course = db.get_or_404(Course, course_id, description="Course not found")
        db.session.delete(course)
        db.session.commit()

        return {"message": "Deleted successfully"}


course_list_fields = {
    'course_id': fields.Integer,
    'course_name': fields.String
}

class AllCourses(Resource):
    # Get all courses
    @roles_required('admin')
    @marshal_with(course_list_fields)
    def get(self):
        all_courses = db.session.scalars(db.select(Course))
        return all_courses
    
