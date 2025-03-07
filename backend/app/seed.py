import os
from datetime import datetime
from flask import current_app
from flask_security import hash_password
from app.security import security
from app.models import db, Course, Video, Assignment, Question
from app.ai_agent.embeddings import process_document



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
        name='instructor'
    )
    security.datastore.create_user(
        email='student@example.com',
        password=hash_password('password'),
        roles=['student'],
        name='student'
    )
    
    populate_sample_data()
    db.session.commit()


def populate_sample_data():
    # create a course
    course = Course(name="Software Engineering", description="Degree Level course")
    db.session.add(course)

    # create 3 more courses
    db.session.add(Course(name="Data Structures", description="Degree Level course"))
    db.session.add(Course(name="Machine Learning", description="Degree Level course"))
    db.session.add(Course(name="Web Development", description="Degree Level course"))

    db.session.commit()

    course_id = course.id
    # add videos for a week
    videos = [  
        ("1.1 Deconstructing the Software Development Process - Introduction", "https://www.youtube.com/watch?v=hKm_rh1RTJQ"),  
        ("1.2 Thinking of Software in terms of Components", "https://www.youtube.com/watch?v=81BaOIrfvJA"),  
        ("1.3 Software Development Process - Requirement Specification", "https://www.youtube.com/watch?v=SU2CBhSFUUA"),  
        ("1.4 Software Development Process - Software Design and Development", "https://www.youtube.com/watch?v=iNqfWUN_hrc"),  
        ("1.5 Testing and Maintenance", "https://www.youtube.com/watch?v=3uokL_BdoiU"),  
        ("1.6 Software Development Models - Waterfall (Plan and Document) Model", "https://www.youtube.com/watch?v=938T0bC7ls0"),  
        ("1.7 Software Development - Agile", "https://www.youtube.com/watch?v=nQzRUGuEDXs"), 
    ]
    for i, (title, url) in enumerate(videos, start=1):
        db.session.add(
            Video(course_id=course_id, week=1, lecture=i, title=title, url=url)
        )
    db.session.commit()

    # add an assignment
    assignment = Assignment(course_id=course_id, week=1, due_date=datetime(2025, 12, 31))
    db.session.add(assignment)
    db.session.commit()

    assignment_id = assignment.id
    # add questions to assignment
    questions = [  
        {  
            'text': "A software company wants to build a website for employee welfare to cater services to its own employees, and thus requires to interact with the employees from different departments. In this case which type of clients are we dealing with?",  
            'option_1': "external users",  
            'option_2': "internal users",  
            'option_3': "software or software components",  
            'option_4': "developers",  
            'correct_option': 2  
        },  
        {  
            'text': "Which of the following tests ensures that the requirements given by the clients are actually met?",  
            'option_1': "Unit testing",  
            'option_2': "Modular testing",  
            'option_3': "Integration testing",  
            'option_4': "Acceptance testing",  
            'correct_option': 4  
        },  
        {  
            'text': "The acceptance testing conducted by a group of selected end users in a real-live environment is called: ",  
            'option_1': "Unit testing",  
            'option_2': "Integration testing",  
            'option_3': "Alpha testing",  
            'option_4': "Beta testing",  
            'correct_option': 4  
        },  
        {  
            'text': "Consider X is a software developer working in a renowned software company. **X** is given responsibility to develop a particular component of a big software. After finishing the coding X wants to test the developed component. Identify the type of testing X wants to perform.",  
            'option_1': "Unit testing",  
            'option_2': "Integration testing",  
            'option_3': "Alpha testing",  
            'option_4': "Beta testing",  
            'correct_option': 1  
        },  
        {  
            'text': "An EdTech company got a contract to build an E-learning system for a school. It decides to first focus on the key feature that the school requires - i.e. to create an online attendance module. The team develops, tests and delivers this module to the school, and then starts working on the next module. The software development process followed in this case is similar to",  
            'option_1': "Waterfall model",  
            'option_2': "V-model",  
            'option_3': "Prototype model",  
            'option_4': "Agile model",  
            'correct_option': 4  
        }  
    ]
    for i, q in enumerate(questions, start=1):
        question = Question(
            assignment_id=assignment_id,
            qno=i,
            text=q.get('text'),
            option_1=q.get('option_1'),
            option_2=q.get('option_2'),
            option_3=q.get('option_3'),
            option_4=q.get('option_4'),
            correct_option=q.get('correct_option')
        )
        db.session.add(question)
    
    db.session.commit()


# store embeddings for sample data
def store_initial_embeddings():
    print("Processing embeddings...")
    docs_folder = os.path.join(os.path.dirname(__file__), 'ai_agent', 'documents')
    for folder in os.listdir(docs_folder):
        course_id = None
        if folder.startswith('course_'):
            course_id = int(folder.split('_')[-1])

        for file in os.listdir(os.path.join(docs_folder, folder)):
            file_path = os.path.join(docs_folder, folder, file)
            process_document(file_path, course_id)

