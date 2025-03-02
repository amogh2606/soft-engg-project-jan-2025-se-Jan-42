from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship
from flask_security import UserMixin, RoleMixin
from datetime import datetime


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


# ---------- User related models ----------
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    active: Mapped[bool] = mapped_column(db.Boolean, default=True, nullable=False)
    fs_uniquifier: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    roles = relationship('Role', secondary='user_roles', back_populates='users')
    courses = relationship('Course', secondary='user_courses', back_populates='users')
    chats = relationship('Chat', back_populates='user', cascade='all, delete-orphan')


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(db.String(255))
    users = relationship('User', secondary='user_roles', back_populates='roles')


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), primary_key=True)
    role_id: Mapped[int] = mapped_column(db.ForeignKey('role.id'), primary_key=True)


# ---------- Course related models ----------
class Course(db.Model):
    __tablename__ = 'course'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(db.String, nullable=True)
    users = relationship('User', secondary='user_courses', back_populates='courses')
    videos = relationship('Video', back_populates='course')
    assignments = relationship('Assignment', back_populates='course', cascade='all, delete-orphan')
    feedbacks = relationship('Feedback', back_populates='course', cascade='all, delete-orphan')


class UserCourses(db.Model):
    __tablename__ = 'user_courses'
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), primary_key=True)
    course_id: Mapped[int] = mapped_column(db.ForeignKey('course.id'), primary_key=True)


class Video(db.Model):
    __tablename__ = 'video'
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(db.ForeignKey('course.id'))
    week: Mapped[int] = mapped_column(db.Integer, nullable=False)
    lecture: Mapped[int] = mapped_column(db.Integer, nullable=False)
    title: Mapped[str] = mapped_column(db.String(255), default='')
    url: Mapped[str] = mapped_column(db.String(255), nullable=False)
    rating: Mapped[float] = mapped_column(db.Float)
    course = relationship('Course', back_populates='videos')


class VideoRating(db.Model):
    __tablename__ = 'video_rating'
    id: Mapped[int] = mapped_column(primary_key=True)
    video_id: Mapped[int] = mapped_column(db.ForeignKey('video.id', ondelete='CASCADE'), nullable=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    rating: Mapped[int] = mapped_column(db.Integer, nullable=False)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(db.ForeignKey('course.id'), nullable=False)
    created: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    title: Mapped[str] = mapped_column(db.String(255), default='Untitled Feedback')
    text: Mapped[str] = mapped_column(db.Text)
    course = relationship('Course', back_populates='feedbacks')


class Assignment(db.Model):
    __tablename__ = 'assignment'
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(db.ForeignKey('course.id'), nullable=False)
    week: Mapped[int] = mapped_column(db.Integer, nullable=False)
    due_date: Mapped[datetime] = mapped_column(db.DateTime, nullable=False)
    course = relationship('Course', back_populates='assignments')
    questions = relationship('Question', back_populates='assignment')


class Question(db.Model):
    __tablename__ = 'question'
    id: Mapped[int] = mapped_column(primary_key=True)
    assignment_id: Mapped[int] = mapped_column(db.ForeignKey('assignment.id'))
    qno: Mapped[int] = mapped_column(db.Integer, nullable=False)
    type: Mapped[str] = mapped_column(db.String(80), default='MCQ')
    text: Mapped[str] = mapped_column(db.Text, nullable=False)
    option1: Mapped[str] = mapped_column(db.String(255), nullable=False)
    option2: Mapped[str] = mapped_column(db.String(255), nullable=False)
    option3: Mapped[str] = mapped_column(db.String(255), nullable=False)
    option4: Mapped[str] = mapped_column(db.String(255), nullable=False)
    correct_option: Mapped[int] = mapped_column(db.Integer, nullable=False)
    assignment = relationship('Assignment', back_populates='questions')


# ---------- Chatbot related models ----------
class Chat(db.Model):
    __tablename__ = 'chat'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    title: Mapped[str] = mapped_column(db.String(255), default='Untitled Chat')
    created: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    active: Mapped[bool] = mapped_column(db.Boolean, default=True, nullable=False)
    bookmarked: Mapped[bool] = mapped_column(db.Boolean, default=False, nullable=False)
    messages = relationship('Message', back_populates='chat', cascade='all, delete-orphan')
    user = relationship('User', back_populates='chats')


class Message(db.Model):
    __tablename__ = 'message'
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(db.ForeignKey('chat.id'), nullable=False)
    text: Mapped[str] = mapped_column(db.Text, default='')
    timestamp: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    is_response: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    chat = relationship('Chat', back_populates='messages')
