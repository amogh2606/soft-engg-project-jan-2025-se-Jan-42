# from flask_sqlalchemy import SQLAlchemy
# from flask_security import UserMixin, RoleMixin
# from datetime import datetime
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from werkzeug.security import generate_password_hash, check_password_hash
#
# db = SQLAlchemy()
#
#
# class User(db.Model, UserMixin):
#     __tablename__ = 'user'
#
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
#     password_hash: Mapped[str] = mapped_column(db.String(255), nullable=False)
#     active: Mapped[bool] = mapped_column(db.Boolean, default=True, nullable=False)
#     fs_uniquifier: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
#
#     roles = relationship('Role', secondary='user_roles', back_populates='users')
#     courses = relationship('Course', secondary='user_courses', back_populates='users')
#     chats = relationship('Chat', back_populates='user', cascade='all, delete-orphan')
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#
# class Role(db.Model, RoleMixin):
#     __tablename__ = 'role'
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
#     description: Mapped[str] = mapped_column(db.String(255))
#     users = relationship('User', secondary='user_roles', back_populates='roles')
#
#
# class UserRoles(db.Model):
#     __tablename__ = 'user_roles'
#     user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#     role_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
#
#
# class Course(db.Model):
#     __tablename__ = 'course'
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(db.String(100), nullable=False)
#     description: Mapped[str] = mapped_column(db.String, nullable=True)
#     users = relationship('User', secondary='user_courses', back_populates='courses')
#     videos = relationship('Video', back_populates='course')
#     assignments = relationship('Assignment', back_populates='course', cascade='all, delete-orphan')
#
#
# class UserCourses(db.Model):
#     __tablename__ = 'user_courses'
#     user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#     course_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
#
#
# class Video(db.Model):
#     __tablename__ = 'video'
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     course_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('course.id'))
#     week: Mapped[int] = mapped_column(db.Integer, nullable=False)
#     lecture: Mapped[int] = mapped_column(db.Integer, nullable=False)
#     title: Mapped[str] = mapped_column(db.String(255), default='')
#     url: Mapped[str] = mapped_column(db.String(255), nullable=False)
#     course = relationship('Course', back_populates='videos')
#
#
# class Assignment(db.Model):
#     __tablename__ = 'assignment'
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     course_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('course.id'), nullable=False)
#     week: Mapped[int] = mapped_column(db.Integer, nullable=False)
#     due_date: Mapped[datetime] = mapped_column(db.DateTime, nullable=False)
#     course = relationship('Course', back_populates='assignments')
#     questions = relationship('Question', back_populates='assignment')
#
#
# class Question(db.Model):
#     __tablename__ = 'question'
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     assignment_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('assignment.id'))
#     qno: Mapped[int] = mapped_column(db.Integer, nullable=False)
#     type: Mapped[str] = mapped_column(db.String(80), default='MCQ')
#     text: Mapped[str] = mapped_column(db.Text, nullable=False)
#     option1: Mapped[str] = mapped_column(db.String(255), nullable=False)
#     option2: Mapped[str] = mapped_column(db.String(255), nullable=False)
#     option3: Mapped[str] = mapped_column(db.String(255), nullable=False)
#     option4: Mapped[str] = mapped_column(db.String(255), nullable=False)
#     correct_option: Mapped[int] = mapped_column(db.Integer, nullable=False)
#     assignment = relationship('Assignment', back_populates='questions')
#
#
# class Chat(db.Model):
#     __tablename__ = 'chat'
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     title: Mapped[str] = mapped_column(db.String(255), default='Untitled Chat')
#     created: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
#     active: Mapped[bool] = mapped_column(db.Boolean, default=True, nullable=False)
#     bookmarked: Mapped[bool] = mapped_column(db.Boolean, default=False, nullable=False)
#     messages = relationship('Message', back_populates='chat', cascade='all, delete-orphan')
#     user = relationship('User', back_populates='chats')
#
#
# class Message(db.Model):
#     __tablename__ = 'message'
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     chat_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
#     text: Mapped[str] = mapped_column(db.Text, default='')
#     timestamp: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
#     is_response: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
#     chat = relationship('Chat', back_populates='messages')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, relationship
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from backend.app.Database import db


# Initialize Flask app


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Fix: Add the missing relationship
    courses = db.relationship('Course', secondary='user_courses', back_populates='users')

    # Relationship for roles
    roles = db.relationship('Role', secondary='user_roles', back_populates='users')

    # Relationship for chat system
    chats = db.relationship('Chat', back_populates='user')


# --- Role Models ---
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))
    users = db.relationship('User', secondary='user_roles', back_populates='roles')


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)


# --- Course Models ---
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=True)

    users = db.relationship('User', secondary='user_courses', back_populates='courses')
    videos = db.relationship('Video', back_populates='course')
    assignments = db.relationship('Assignment', back_populates='course', cascade='all, delete-orphan')


class UserCourses(db.Model):
    __tablename__ = 'user_courses'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)


class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    week = db.Column(db.Integer, nullable=False)
    lecture = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), default='')
    url = db.Column(db.String(255), nullable=False)

    course = db.relationship('Course', back_populates='videos')


class Assignment(db.Model):
    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    week = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

    course = db.relationship('Course', back_populates='assignments')
    questions = db.relationship('Question', back_populates='assignment')


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'))
    qno = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(80), default='MCQ')
    text = db.Column(db.Text, nullable=False)
    option1 = db.Column(db.String(255), nullable=False)
    option2 = db.Column(db.String(255), nullable=False)
    option3 = db.Column(db.String(255), nullable=False)
    option4 = db.Column(db.String(255), nullable=False)
    correct_option = db.Column(db.Integer, nullable=False)

    assignment = db.relationship('Assignment', back_populates='questions')


# --- Chatbot Models ---
class Chat(db.Model):
    __tablename__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), default='Untitled Chat')
    created = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    bookmarked = db.Column(db.Boolean, default=False, nullable=False)

    messages = db.relationship('Message', back_populates='chat', cascade='all, delete-orphan')
    user = db.relationship('User', back_populates='chats')


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    text = db.Column(db.Text, default='')
    timestamp = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    is_response = db.Column(db.Boolean, nullable=False)

    chat = db.relationship('Chat', back_populates='messages')
