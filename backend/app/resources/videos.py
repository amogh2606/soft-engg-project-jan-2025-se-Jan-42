from flask import request
from flask_restful import Resource
from flask_security import current_user, auth_required  # or login_required
from sqlalchemy.exc import IntegrityError

from backend.app.models import Video, Course, db


class VideoResource(Resource):
    @auth_required()
    def get(self, video_id):
        """Get video details"""
        video = Video.query.get_or_404(video_id)

        # Check if user has access (enrolled in course or admin)
        if (current_user not in video.course.users and
            not current_user.has_role('admin')):
            return {'message': 'Unauthorized'}, 403

        return {
            'id': video.id,
            'course_id': video.course_id,
            'week': video.week,
            'lecture': video.lecture,
            'title': video.title,
            'url': video.url
        }, 200

    @auth_required()
    def put(self, video_id):
        """Update video details (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        video = Video.query.get_or_404(video_id)
        data = request.get_json() or {}

        try:
            if 'week' in data:
                video.week = data['week']
            if 'lecture' in data:
                video.lecture = data['lecture']
            if 'title' in data:
                video.title = data['title']
            if 'url' in data:
                video.url = data['url']
            if 'course_id' in data:
                # Verify new course exists
                Course.query.get_or_404(data['course_id'])
                video.course_id = data['course_id']

            db.session.commit()
            return {'message': 'Video updated successfully'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

    @auth_required()
    def delete(self, video_id):
        """Delete a video (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        video = Video.query.get_or_404(video_id)
        try:
            db.session.delete(video)
            db.session.commit()
            return {'message': 'Video deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class VideoListResource(Resource):
    @auth_required()
    def get(self, course_id=None):
        """Get all videos, optionally filtered by course"""
        if course_id:
            course = Course.query.get_or_404(course_id)
            # Check if user has access
            if (current_user not in course.users and
                not current_user.has_role('admin')):
                return {'message': 'Unauthorized'}, 403
            videos = Video.query.filter_by(course_id=course_id).all()
        else:
            # Admin sees all videos, regular users see only their courses' videos
            if current_user.has_role('admin'):
                videos = Video.query.all()
            else:
                videos = [video for course in current_user.courses
                         for video in course.videos]

        return [{
            'id': video.id,
            'course_id': video.course_id,
            'week': video.week,
            'lecture': video.lecture,
            'title': video.title,
            'url': video.url
        } for video in videos], 200

    @auth_required()
    def post(self):
        """Create a new video (admin only)"""
        if not current_user.has_role('admin'):
            return {'message': 'Admin access required'}, 403

        data = request.get_json() or {}
        required_fields = ['course_id', 'week', 'lecture', 'url']
        if not all(field in data for field in required_fields):
            return {'message': 'Missing required fields'}, 400

        try:
            # Verify course exists
            Course.query.get_or_404(data['course_id'])

            video = Video(
                course_id=data['course_id'],
                week=data['week'],
                lecture=data['lecture'],
                title=data.get('title', ''),
                url=data['url']
            )
            db.session.add(video)
            db.session.commit()
            return {
                'message': 'Video created successfully',
                'id': video.id
            }, 201

        except IntegrityError:
            db.session.rollback()
            return {'message': 'Video creation failed - possible duplicate'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
