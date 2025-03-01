from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from backend.app.models import User, Course


class UserCoursesResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        courses = [{'id': course.id, 'name': course.name, 'description': course.description} for course in user.courses]
        return jsonify({'user_id': user_id, 'courses': courses})


class CourseUsersResource(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.query.get(course_id)
        if not course:
            return {'message': 'Course not found'}, 404

        users = [{'id': user.id, 'email': user.email} for user in course.users]
        return jsonify({'course_id': course_id, 'users': users})
