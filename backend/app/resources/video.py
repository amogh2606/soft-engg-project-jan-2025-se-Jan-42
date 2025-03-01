


from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from backend.app import db
from backend.app.models import Course, Video


def is_admin():
    identity = get_jwt_identity()
    return identity== 'admin'

class CourseVideosResource(Resource):
    def get(self, course_id):
        course = Course.query.get(course_id)
        if not course:
            return {'message': 'Course not found'}, 404

        videos = [
            {
                'id': video.id,
                'week': video.week,
                'lecture': video.lecture,
                'title': video.title,
                'url': video.url
            }
            for video in course.videos
        ]
        return {'course_id': course.id, 'course_name': course.name, 'videos': videos}


class VideoResource(Resource):
    @jwt_required()
    def get(self, video_id=None):
        if video_id:
            video = Video.query.get(video_id)
            return {
                'id': video.id,
                'course_id': video.course_id,
                'week': video.week,
                'lecture': video.lecture,
                'title': video.title,
                'url': video.url
            }
        videos= Video.query.all()
        return jsonify(
            [{'id': video.id, 'course_id': video.course_id, 'week': video.week, 'lecture': video.lecture, 'title': video.title, 'url': video.url} for video in videos]
        )



    @jwt_required()
    def post(self):
        if not is_admin():
            return {'message': 'Admin access required'}, 403

        data = request.get_json()
        new_video = Video(
            course_id=data.get('course_id'),
            week=data.get('week'),
            lecture=data.get('lecture'),
            title=data.get('title', ''),
            url=data.get('url')
        )
        db.session.add(new_video)
        db.session.commit()
        return {'message': 'Video added successfully', 'video_id': new_video.id}, 201

    @jwt_required()
    def put(self, video_id):
        if not is_admin():
            return {'message': 'Admin access required'}, 403

        video = Video.query.get(video_id)
        if not video:
            return {'message': 'Video not found'}, 404

        data = request.get_json()
        video.week = data.get('week', video.week)
        video.lecture = data.get('lecture', video.lecture)
        video.title = data.get('title', video.title)
        video.url = data.get('url', video.url)

        db.session.commit()
        return {'message': 'Video updated successfully'}

    @jwt_required()
    def delete(self, video_id):
        if not is_admin():
            return {'message': 'Admin access required'}, 403

        video = Video.query.get(video_id)
        if not video:
            return {'message': 'Video not found'}, 404

        db.session.delete(video)
        db.session.commit()
        return {'message': 'Video deleted successfully'}, 200
