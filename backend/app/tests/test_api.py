import json
import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api"
LOG_FILE = "tests/api_responses.log"

admin_creds = {"email": "admin@example.com", "password": "password"}
instructor_creds = {"email": "instructor@example.com", "password": "password"}
student_creds = {"email": "testing3@example.com", "password": "password123"}

admin_session = None
instructor_session = None
student_session = None

def log_response(endpoint, response):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"Endpoint: {endpoint}\n")
        log_file.write(f"Status Code: {response.status_code}\n")
        try:
            log_file.write(f"Response Body: {json.dumps(response.json(), indent=2)}\n")
        except Exception:
            log_file.write("Response Body: Non-JSON response\n")
        log_file.write("-" * 50 + "\n")


@pytest.fixture(scope="module", autouse=True)
def setup():
    global admin_session, instructor_session, student_session

    admin_response = requests.post(f"{BASE_URL}/login", json=admin_creds)
    admin_session = admin_response.cookies.get("session")

    instructor_response = requests.post(f"{BASE_URL}/login", json=instructor_creds)
    instructor_session = instructor_response.cookies.get("session")

    student_response = requests.post(f"{BASE_URL}/login", json=student_creds)
    student_session = student_response.cookies.get("session")


def auth_headers(session_cookie):
    return {"Cookie": f"session={session_cookie}", "Content-Type": "application/json"}


# def test_user_registration_valid():
#     url = f"{BASE_URL}/user"
#     payload = {
#         "email": f"testing3@example.com",
#         "password": "password123",
#         "name": "Tester Kumar"
#     }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 201
#     assert response.json()["message"] == "Registered successfully"

# def test_user_registration_weak_password():
#     url = f"{BASE_URL}/user"
#     payload = {
#         "email": "weakpass@example.com",
#         "password": "12345",
#         "name": "Weak Password User"
#     }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 400

# def test_login_nonexistent_email():
#     url = f"{BASE_URL}/login"
#     payload = {
#         "email": "nonexistent@example.com",
#         "password": "password123"
#     }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 401


# def test_login_valid():
#     url = f"{BASE_URL}/login"
#     payload = {
#         "email": "testing3@example.com",
#         "password": "password123"
#     }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200
#     assert response.json()["message"] == "Logged in successfully"


# def test_login_invalid_password():
#     url = f"{BASE_URL}/login"
#     payload = {
#         "email": admin_creds["email"],
#         "password": "wrongpassword"
#     }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 401
#     assert response.json()["message"] == "Invalid credentials"


# def test_fetch_user_profile():
#     url = f"{BASE_URL}/user"
#     headers = auth_headers(student_session)
#     response = requests.get(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200
#     user_data = response.json()    
#     assert user_data["email"] == student_creds["email"]

# def test_update_user_profile():
#     url = f"{BASE_URL}/user"
#     payload = {
#         "email": "updated_email@example.com",
#         "name": "Updated Name"
#     }
#     headers = auth_headers(student_session)
#     response = requests.put(url, json=payload, headers=headers)
#     log_response(url, response)   
#     assert response.status_code == 200
#     assert response.json()["message"] == "Updated successfully"

# def test_delete_user():
#     user_id = 8
#     url = f"{BASE_URL}/user/{user_id}"
#     headers = auth_headers(admin_session)
#     response = requests.delete(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200
#     assert response.json()["message"] == "Deleted successfully"


# def test_fetch_all_courses():
#     url = f"{BASE_URL}/courses/all"
#     headers = auth_headers(student_session) 
#     response = requests.get(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200, "Failed to fetch courses"

# def test_enroll_user_in_course():
#     url = f"{BASE_URL}/courses/enroll"
#     payload = {
#         "course_id": 1,
#         "user_id": 2
#     }
#     headers = auth_headers(admin_session)
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 201, "Failed to enroll user in course"
#     assert response.json()["message"] == "Enrolled successfully"

# def test_fetch_enrolled_users():
#     course_id = 1
#     url = f"{BASE_URL}/enrollments/{course_id}"
#     headers = auth_headers(admin_session)
#     response = requests.get(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200, f"Failed to fetch enrolled users for course {course_id}"

# def test_assign_instructor_to_multiple_courses():
#     enroll_url = f"{BASE_URL}/courses/enroll"
#     payload_course_1 = {
#         "course_id": 3,
#         "user_id": 5
#     }
#     headers = auth_headers(admin_session)
#     response_course_1 = requests.post(enroll_url, json=payload_course_1, headers=headers)
#     log_response(enroll_url, response_course_1)
#     assert response_course_1.status_code == 400
#     assert response_course_1.json()["message"] == "Instructor already assigned to a course"

# def test_delete_course_with_active_users():
#     delete_url = f"{BASE_URL}/courses/1"
#     headers = auth_headers(admin_session)
#     delete_response = requests.delete(delete_url, headers=headers)
#     log_response(delete_url, delete_response)
#     assert delete_response.status_code == 200
#     assert delete_response.json()["message"] == "Course Deleted"

# def test_access_for_course_creation():
#     url = f"{BASE_URL}/courses"
#     payload = {
#         "name": "AI-SMPS",
#         "description": "An AI course"
#     }
#     instructor_headers = auth_headers(instructor_session)
#     instructor_response = requests.post(url, json=payload, headers=instructor_headers)
#     log_response(url, instructor_response)
#     assert instructor_response.json() == {
#   "meta": {
#     "code": 403
#   },
#   "response": {
#     "errors": [
#       "You do not have permission to view this resource."
#     ]
#   }
# }

# def test_generate_video_summary():
#     video_id = 1
#     url = f"{BASE_URL}/videos/{video_id}/summary"
#     headers = auth_headers(student_session)
#     response = requests.post(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200

# def test_assignment_retrieval_auth_user():
#     assignment_id = 7
#     url = f"{BASE_URL}/assignments/{assignment_id}"
#     headers = auth_headers(student_session)
#     response = requests.get(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200

# def test_start_new_chat_session():
#     url = f"{BASE_URL}/chats"
#     headers = auth_headers(student_session)
#     response = requests.post(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200

# def test_chatbot_interaction():
#     chatbot_url = f"{BASE_URL}/chatbot"
#     payload = {
#         "chat_id": 2, # Must be active
#         "query": "What is software engineering?"
#     }
#     headers = auth_headers(student_session)
#     chatbot_response = requests.post(chatbot_url, json=payload, headers=headers)
#     log_response(chatbot_url, chatbot_response)   
#     assert chatbot_response.status_code == 200

# def test_course_specific_query():
#     chatbot_url = f"{BASE_URL}/chatbot"
#     payload = {
#         "chat_id": 2,
#         "course_id": 3,
#         "query": "What topics are covered in this course?"
#     }
#     headers = auth_headers(student_session)
#     response = requests.post(chatbot_url, json=payload, headers=headers)
#     log_response(chatbot_url, response)
#     assert response.status_code == 200

# def test_chatbot_response_to_ambiguous_query():
#     chatbot_url = f"{BASE_URL}/chatbot"
#     payload = {
#         "chat_id": 2,
#         "query": "Can you explain that topic ?"
#     }
#     headers = auth_headers(student_session)
#     response = requests.post(chatbot_url, json=payload, headers=headers)
#     log_response(chatbot_url, response)
#     assert response.status_code == 200
#     response_message = response.json()["message"].lower()
#     assert any(phrase in response_message for phrase in [
#         "clarify", 
#         "more specific", 
#         "please elaborate", 
#         "which topic",
#         "could you specify"
#     ])

# def test_retrieve_uploaded_documents_for_course():
#     course_id = 1
#     url = f"{BASE_URL}/documents/{course_id}"
#     headers = auth_headers(instructor_session)
#     response = requests.get(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200


# def test_retrieve_faqs_with_auth():
#     url = f"{BASE_URL}/faqs"
#     headers = auth_headers(instructor_session)
#     response = requests.get(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200

# def test_start_new_chat_with_existing_active_session():
#     url = f"{BASE_URL}/chats"
#     headers = auth_headers(student_session)
#     response1 = requests.post(url, headers=headers)
#     first_chat_id = response1.json()["id"]
#     response2 = requests.post(url, headers=headers)
#     second_chat_id = response2.json()["id"]
#     get_url_first = f"{BASE_URL}/chats/{first_chat_id}"
#     response_get_first = requests.get(get_url_first, headers=headers)
#     log_response(get_url_first, response_get_first)    
#     assert not response_get_first.json()["active"]
#     get_url_second = f"{BASE_URL}/chats/{second_chat_id}"
#     response_get_second = requests.get(get_url_second, headers=headers)
#     log_response(get_url_second, response_get_second)
#     assert response_get_second.json()["active"]

# def test_submit_feedback():
#     course_id = 1
#     url = f"{BASE_URL}/feedback/{course_id}"
#     headers = auth_headers(student_session)
#     payload = {
#         "title": "Great course!",
#         "text": "The lectures were very informative and engaging."
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 201
#     assert response.json()["message"] == "Feedback submitted successfully"

# def test_retrieve_feedback():
#     course_id = 1
#     url = f"{BASE_URL}/feedback/{course_id}"
#     headers = auth_headers(instructor_session)
#     response = requests.get(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200
#     feedback_list = response.json()
#     assert isinstance(feedback_list, list)

# def test_submit_feedback_non_enrolled_course():
#     non_enrolled_course_id = 3
#     url = f"{BASE_URL}/feedback/{non_enrolled_course_id}"
#     headers = auth_headers(student_session)
    
#     payload = {
#         "title": "Great course!",
#         "text": "The lectures were very informative and engaging."
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 400

# def test_logout():
#     url = f"{BASE_URL}/logout" 
#     headers = auth_headers(student_session) 
#     response = requests.post(url, headers=headers)
#     log_response(url, response)
#     assert response.status_code == 200
#     assert response.json()["message"] == "Logged out successfully"
