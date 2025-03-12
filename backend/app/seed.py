import os, csv
from datetime import datetime
from flask import current_app
from flask_security import hash_password
from app.security import security
from app.models import db, Course, Video, Assignment, Question
from app.ai_agent.embeddings import client, process_document



# populate initial db data
def seed_db():
    # check if db already created
    db_path = os.path.join(current_app.instance_path, 'app_db.sqlite3')
    if os.path.exists(db_path):
        return
    
    db.create_all()
    # create roles
    security.datastore.find_or_create_role(name='admin', description='The admin')
    security.datastore.find_or_create_role(name='instructor', description='Instructor / TA')
    security.datastore.find_or_create_role(name='student', description='Student - primary user')
    # create users
    security.datastore.create_user(
        email='admin@example.com',
        password=hash_password('password'),
        roles=['admin'],
        name='ADMIN'
    )
    security.datastore.create_user(
        email='instructor@example.com',
        password=hash_password('password'),
        roles=['instructor'],
        name='Instructor 1'
    )
    security.datastore.create_user(
        email='student@example.com',
        password=hash_password('password'),
        roles=['student'],
        name='Student 1'
    )
    
    populate_course_data()
    db.session.commit()


def populate_course_data():
    # create courses
    courses = [
        Course(name="Software Engineering", description="Degree Level course"),
        Course(name="Software Testing", description="Degree Level course"),
        Course(name="Machine Learning Pratice", description="Diploma Level course"),
        Course(name="English I", description="Foundation Level course")
    ]
    db.session.add_all(courses)
    db.session.flush()

    # add course data from csv files
    for course in courses:
        course_folder = os.path.join(os.getcwd(), 'data', f'course_{course.id}')
        # if course data folder does not exist, remove the course
        if not os.path.exists(course_folder):
            db.session.delete(course)
            continue

        # add lecture videos
        file_path = os.path.join(course_folder, 'videos.csv')
        if os.path.exists(file_path):
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    video = Video(
                        course_id=course.id,
                        week=int(row.get('week')),
                        lecture=int(row.get('lecture')),
                        title=row.get('title'),
                        url=row.get('url')
                    )
                    db.session.add(video)

        # create assignments
        n_weeks = 2
        assignments = {}
        for i in range(1, n_weeks+1):
            assignments[i] = Assignment(course_id=course.id, week=i, due_date=datetime(2025, 12, 31))
            db.session.add(assignments[i])
        
        db.session.flush()
        # add questions to assignments
        file_path = os.path.join(course_folder, 'questions.csv')
        if os.path.exists(file_path):
            with open(file_path, encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    week = int(row.get('week'))
                    if week not in assignments:
                        continue
                    assignment_id = assignments[week].id
                    question = Question(
                        assignment_id=assignment_id,
                        qno=int(row.get('qno')),
                        text=row.get('text'),
                        option_1=row.get('option_1'),
                        option_2=row.get('option_2'),
                        option_3=row.get('option_3'),
                        option_4=row.get('option_4'),
                        correct_option=int(row.get('correct_option'))
                    )
                    db.session.add(question)

        db.session.commit()
  
    
# store embeddings for course data
def process_embeddings():
    print("Processing embeddings...")
    client.reset()

    docs_folder = os.path.join(os.path.dirname(__file__), 'ai_agent', 'documents')
    for folder in os.listdir(docs_folder):
        course_id = None
        if folder.startswith('course_'):
            course_id = int(folder.split('_')[-1])

        for file in os.listdir(os.path.join(docs_folder, folder)):
            file_path = os.path.join(docs_folder, folder, file)
            process_document(file_path, course_id)

