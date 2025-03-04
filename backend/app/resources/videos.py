from flask_restful import Resource, reqparse, marshal_with, fields, abort
from flask_security import roles_required, auth_required, current_user
from app.models import db, Video, Course, VideoRating



video_fields = {
    'id': fields.Integer,
    'course_id': fields.Integer,
    'week': fields.Integer,
    'lecture': fields.Integer,
    'title': fields.String,
    'url': fields.String,
    'rating': fields.Float
}

class VideoResource(Resource):
    # Get a specific video
    @auth_required
    @marshal_with(video_fields)
    def get(self, video_id):
        video = db.get_or_404(Video, video_id, description='Video not found')

        if not current_user.has_role('admin'):
            if video.course not in current_user.courses:
                abort(400, message="Course not enrolled")
                   
        return video


    # Add a new video
    @roles_required('admin')
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('course_id', type=int, nullable=False)
        parser.add_argument('week', required=True, type=int, nullable=False, choices=range(1, 13))
        parser.add_argument('lecture', required=True, type=int, nullable=False)
        parser.add_argument('title', required=True, nullable=False)
        parser.add_argument('url', required=True, nullable=False)

        args = parser.parse_args()
        course_id = args.get('course_id')
        title = args.get('title')
        week = args.get('week')
        lecture = args.get('lecture')
        url = args.get('url')

        if course_id:
            db.get_or_404(Course, course_id, description='Course not found')
        
        if db.session.scalar(db.select(Video).filter_by(url=url)):
            abort(400, message="Video already exists")

        new_video = Video(course_id=course_id, title=title, week=week, lecture=lecture, url=url)
        db.session.add(new_video)
        db.session.commit()

        return {"message": "Video added successfully"}, 201
    

    # Update a specific video
    @roles_required('admin')
    def put(self, video_id):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('course_id', type=int)
        parser.add_argument('week', type=int, choices=range(1, 13))
        parser.add_argument('lecture', type=int)
        parser.add_argument('title')
        parser.add_argument('url')

        video = db.get_or_404(Video, video_id, description="Video not found")

        args = parser.parse_args()
        course_id = args.get('course_id')
        title = args.get('title')
        week = args.get('week')
        lecture = args.get('lecture')
        url = args.get('url')

        if course_id:
            db.get_or_404(Course, course_id, description='Course not found')
            video.course_id = course_id

        if title: video.title = title
        if week: video.week = week
        if lecture: video.lecture = lecture
        if url: video.url = url

        db.session.commit()
        return {"message": "Updated successfully"}


    # Delete a specific video
    @roles_required('admin')
    def delete(self, video_id):
        video = db.get_or_404(Video, video_id, description="Video not found")
        db.session.delete(video)
        db.session.commit()

        return {"message": "Deleted successfully"}


video_list_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'url': fields.String
}

class AllVideos(Resource):
    # Get all videos
    @roles_required('admin')
    @marshal_with(video_list_fields)
    def get(self):
        all_videos = db.session.scalars(db.select(Video))
        return all_videos


class RateVideo(Resource):
    # Rate a video
    @roles_required('student')
    def post(self, video_id):
        parser = reqparse.RequestParser()
        parser.add_argument('rating', type=int, required=True, nullable=False, choices=range(1, 6))

        args = parser.parse_args()
        rating = args.get('rating')

        video = db.get_or_404(Video, video_id, description="Video not found")
        if video.course not in current_user.courses:
            abort(400, message="You cannot rate this video")

        stmt = db.select(VideoRating).filter_by(video_id=video_id, user_id=current_user.id)
        if db.session.scalar(stmt):
            abort(400, message="Already rated")

        new_rating = VideoRating(video_id=video_id, user_id=current_user.id, rating=rating)
        db.session.add(new_rating)
        db.session.flush()
        self.update_video_rating(video_id)

        db.session.commit()
        return {"message": "Rated successfully"}, 201


    def update_video_rating(self, video_id):
        video = db.get_or_404(Video, video_id, description="Video not found")
        stmt = db.select(VideoRating.rating).filter_by(video_id=video_id)
        ratings = db.session.scalars(stmt).all()
        avg_rating = sum(ratings) / len(ratings)
        video.rating = round(avg_rating, 1)
        
