# with app.app_context():
#     db.create_all()
#
#     # Create roles
#     admin_role = Role(name='admin', description='Administrator')
#     user_role = Role(name='user', description='Regular user')
#     db.session.add_all([admin_role, user_role])
#     db.session.commit()
#
#     # Create users
#     users = []
#     for i in range(3):
#         user = User(
#             email=f'user{i + 1}@example.com',
#             password='hashed_password',  # Replace with hashed password
#             active=True,
#             fs_uniquifier=f'unique_{i + 1}'
#         )
#         user.roles.append(user_role if i > 0 else admin_role)
#         users.append(user)
#
#     db.session.add_all(users)
#     db.session.commit()
#
#     # Create courses
#     courses = []
#     for i in range(2):
#         course = Course(
#             name=f'Course {i + 1}',
#             description=f'Description for Course {i + 1}'
#         )
#         courses.append(course)
#     db.session.add_all(courses)
#     db.session.commit()
#
#     # Assign users to courses
#     for user in users:
#         for course in courses:
#             user_course = UserCourses(user_id=user.id, course_id=course.id)
#             db.session.add(user_course)
#     db.session.commit()
#
#     # Create videos for courses
#     for course in courses:
#         for week in range(1, 3):
#             for lecture in range(1, 3):
#                 video = Video(
#                     course_id=course.id,
#                     week=week,
#                     lecture=lecture,
#                     title=f'Week {week} Lecture {lecture}',
#                     url=f'https://example.com/video{week}{lecture}'
#                 )
#                 db.session.add(video)
#     db.session.commit()
#
#     # Create assignments
#     assignments = []
#     for course in courses:
#         for week in range(1, 3):
#             assignment = Assignment(
#                 course_id=course.id,
#                 week=week,
#                 due_date=datetime(2025, 3, week + 1, 23, 59)
#             )
#             assignments.append(assignment)
#     db.session.add_all(assignments)
#     db.session.commit()
#
#     # Create questions for assignments
#     for assignment in assignments:
#         for qno in range(1, 3):
#             question = Question(
#                 assignment_id=assignment.id,
#                 qno=qno,
#                 text=f'Question {qno} for assignment {assignment.id}',
#                 option1='Option A',
#                 option2='Option B',
#                 option3='Option C',
#                 option4='Option D',
#                 correct_option=random.randint(1, 4)
#             )
#             db.session.add(question)
#     db.session.commit()
#
#     # Create chat history
#     for user in users:
#         chat = Chat(user_id=user.id, title=f'Chat with {user.email}')
#         db.session.add(chat)
#         db.session.commit()
#
#         for i in range(3):
#             message = Message(
#                 chat_id=chat.id,
#                 text=f'Message {i + 1} from {user.email}',
#                 is_response=random.choice([True, False])
#             )
#             db.session.add(message)
#     db.session.commit()
