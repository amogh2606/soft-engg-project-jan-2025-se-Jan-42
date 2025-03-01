from importlib.resources import Resource

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from backend.app import db
from backend.app.models import Course, User


class CourseResource(Resource):
    @jwt_required()
    def get(self, course_id=None):
        """Retrieve all courses or a specific course by ID"""
        if course_id:
            course = Course.query.get_or_404(course_id)
            return jsonify({"id": course.id, "name": course.name, "description": course.description})

        courses = Course.query.all()
        return jsonify(
            [{"id": course.id, "name": course.name, "description": course.description} for course in courses])

    @jwt_required()
    def post(self):
        """Create a new course (Admin only)"""
        identity = get_jwt_identity()  # Now identity is a dictionary
        print(identity)
        is_admin = identity=="admin"

        if not is_admin:
            return {"message": "Unauthorized"}, 403

        data = request.json
        new_course = Course(name=data['course_name'], description=data.get('description'))
        db.session.add(new_course)
        db.session.commit()

        return jsonify({"id": new_course.id, "name": new_course.name, "description": new_course.description})


    @jwt_required()
    def delete(self, course_id):
        if not get_jwt_identity()=="admin":
            return {"message": "Unauthorized"}, 403
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return {"message": "Course deleted"}

class AssignCourseResource(Resource):
    @jwt_required()
    def post(self):
        if not get_jwt_identity()=="admin":
            return {"message": "Unauthorized"}, 403
        data = request.json
        user = User.query.get(data['user_id'])
        course = Course.query.get(data['course_id'])
        if not user or not course:
            return {"message": "User or Course not found"}, 404
        user.courses.append(course)
        db.session.commit()
        return {"message": "Course assigned successfully"}

class DeassignCourseResource(Resource):
    @jwt_required()
    def post(self):
        if not get_jwt_identity()=="admin":
            return {"message": "Unauthorized"}, 403
        data = request.json
        user = User.query.get(data['user_id'])
        course = Course.query.get(data['course_id'])
        if not user or not course:
            return {"message": "User or Course not found"}, 404
        user.courses.remove(course)
        db.session.commit()
        return {"message": "Course deassigned successfully"}


