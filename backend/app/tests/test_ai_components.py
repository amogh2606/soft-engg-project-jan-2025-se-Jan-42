import pytest
import requests
import os
import json

BASE_URL = "http://127.0.0.1:5000/api"
LOG_FILE = "tests/ai_testing.log"

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

def auth_headers(session_cookie):
    return {"Cookie": f"session={session_cookie}", "Content-Type": "application/json"}

@pytest.fixture(scope="module", autouse=True)
def setup_ai_tests():
    global admin_session, instructor_session, student_session
    
    with open(LOG_FILE, "w") as log_file:
        log_file.write("AI Testing Log\n")
    
    from test_api import admin_session as admin_s
    from test_api import instructor_session as instructor_s
    from test_api import student_session as student_s
    
    admin_session = admin_s
    instructor_session = instructor_s
    student_session = student_s
    if not admin_session:
        admin_creds = {"email": "admin@example.com", "password": "password"}
        admin_response = requests.post(f"{BASE_URL}/login", json=admin_creds)
        admin_session = admin_response.cookies.get("session")
    
    if not instructor_session:
        instructor_creds = {"email": "instructor@example.com", "password": "password"}
        instructor_response = requests.post(f"{BASE_URL}/login", json=instructor_creds)
        instructor_session = instructor_response.cookies.get("session")
    
    if not student_session:
        student_creds = {"email": "updated_email@example.com", "password": "password123"}
        student_response = requests.post(f"{BASE_URL}/login", json=student_creds)
        student_session = student_response.cookies.get("session")
    
    yield

def create_chat_session(session_cookie):
    chat_url = f"{BASE_URL}/chats"
    response = requests.post(chat_url, headers=auth_headers(session_cookie))
    return response.json()["id"]

# class TestChatbotAI:
#     def test_chatbot_response_quality(self):
#         chat_id = create_chat_session(student_session)    
#         chatbot_url = f"{BASE_URL}/chatbot"
#         query_payload = {
#             "chat_id": chat_id,
#             "query": "What is the software development life cycle?"
#         }
#         response = requests.post(chatbot_url, json=query_payload, headers=auth_headers(student_session))
#         log_response(chatbot_url, response)
#         assert response.status_code == 200
#         response_text = response.json()["message"].lower()
#         sdlc_terms = ["requirement", "design", "development", "testing", "deployment", "maintenance"]
#         matches = [term for term in sdlc_terms if term in response_text]    
#         assert len(matches) >= 3
    
#     def test_chatbot_context_awareness(self):
#         chat_id = create_chat_session(student_session)    
#         chatbot_url = f"{BASE_URL}/chatbot"
#         first_query = {
#             "chat_id": chat_id,
#             "query": "What is software testing?"
#         }
#         first_response = requests.post(chatbot_url, json=first_query, headers=auth_headers(student_session))
#         log_response(f"{chatbot_url} (first query)", first_response)
#         follow_up_query = {
#             "chat_id": chat_id,
#             "query": "Are there different levels to do so, can you name them?"
#         }
#         follow_up_response = requests.post(chatbot_url, json=follow_up_query, headers=auth_headers(student_session))
#         log_response(f"{chatbot_url} (follow-up)", follow_up_response)        
#         assert follow_up_response.status_code == 200
#         response_text = follow_up_response.json()["message"].lower()
#         assert "software testing" in response_text or "testing" in response_text, "Response doesn't maintain context"
    
#     def test_course_specific_knowledge(self):
#         chat_id = create_chat_session(student_session)        
#         chatbot_url = f"{BASE_URL}/chatbot"
#         query_payload = {
#             "chat_id": chat_id,
#             "course_id": 1,
#             "query": "What are the key concepts in this course?"
#         }
#         response = requests.post(chatbot_url, json=query_payload, headers=auth_headers(student_session))
#         log_response(chatbot_url, response)        
#         assert response.status_code == 200
#         response_text = response.json()["message"].lower()
#         se_concepts = ["software", "development", "engineering", "sdlc", "agile", "waterfall", "requirements"]
#         matches = [concept for concept in se_concepts if concept in response_text]        
#         assert len(matches) >= 2, f"Response doesn't mention software engineering concepts. Found: {matches}"

# class TestAssignmentHelpAI:
#     def test_assignment_help_quality(self):
#         assignment_id = 1  
#         url = f"{BASE_URL}/assignments/{assignment_id}"
#         assignment_response = requests.get(url, headers=auth_headers(student_session))
#         if assignment_response.status_code != 200 or not assignment_response.json().get("questions"):
#             pytest.skip("No questions available for testing")       
#         question = assignment_response.json()["questions"][0]
#         question_id = question["id"]
#         correct_option = question["correct_option"]
#         course_id = assignment_response.json()["course_id"]
#         help_url = f"{BASE_URL}/assignments/help"
#         payload = {
#             "question_id": question_id,
#             "assignment_id": assignment_id,
#             "course_id": course_id
#         }       
#         help_response = requests.post(help_url, json=payload, headers=auth_headers(student_session))
#         log_response(help_url, help_response)
        
#         assert help_response.status_code == 200
#         hint_text = help_response.json()["message"].lower()       
#         assert len(hint_text) > 50, "Hint is too short to be helpful"
#         correct_text = question[f"option_{correct_option}"].lower()
#         assert correct_text not in hint_text, "Hint reveals the correct answer"
#         assert str(correct_option) not in hint_text, "Hint reveals the correct option number"

# class TestVideoFeaturesAI:
#     def test_video_summary_quality(self):
#         videos_url = f"{BASE_URL}/videos/all"
#         videos_response = requests.get(videos_url, headers=auth_headers(admin_session))      
#         if videos_response.status_code != 200 or not videos_response.json():
#             pytest.skip("No videos available for testing")      
#         video_id = videos_response.json()[0]["id"]
#         summary_url = f"{BASE_URL}/videos/{video_id}/summary"     
#         response = requests.post(summary_url, headers=auth_headers(student_session))
#         log_response(summary_url, response)     
#         assert response.status_code == 200
#         summary = response.json()["summary"]      
#         assert len(summary) > 100, "Summary is too short"
#         assert "." in summary, "Summary lacks proper sentences"
#         assert len(summary.split(".")) > 3, "Summary has too few sentences"
#         low_quality_indicators = ["i don't know", "i'm not sure", "i cannot", "as an ai"]
#         for indicator in low_quality_indicators:
#             assert indicator not in summary.lower(), f"Summary contains low-quality indicator: {indicator}"
    
#     def test_quiz_generation_quality(self):
#         videos_url = f"{BASE_URL}/videos/all"
#         videos_response = requests.get(videos_url, headers=auth_headers(admin_session))      
#         if videos_response.status_code != 200 or not videos_response.json():
#             pytest.skip("No videos available for testing")     
#         video_id = videos_response.json()[0]["id"]
#         quiz_url = f"{BASE_URL}/videos/{video_id}/quiz"       
#         response = requests.post(quiz_url, headers=auth_headers(student_session))
#         log_response(quiz_url, response)      
#         assert response.status_code == 200
#         quiz = response.json()["quiz"]
#         option_patterns = ["A)", "B)", "C)", "D)", "1.", "2.", "3.", "4."]
#         has_options = any(pattern in quiz for pattern in option_patterns)
#         assert has_options, "Quiz doesn't have proper option format"
#         question_count = 0
#         lines = quiz.split('\n')
#         for i, line in enumerate(lines):
#             if any(f"{num}." in line or f"{num})" in line for num in range(1, 10)):
#                 question_count += 1    
#         assert question_count >= 3, f"Quiz has too few questions: {question_count}"

# class TestDocumentEmbeddingsAI:
#     def test_document_upload_and_influence_responses(self):
#         test_content = """
#         The first thing to do in software testing is to learn biology.
#         """      
#         test_filename = "test_document2.txt"
#         with open(test_filename, "w") as f:
#             f.write(test_content)

#         course_id = 1
#         upload_url = f"{BASE_URL}/documents/{course_id}"
        
#         with open(test_filename, "rb") as f:
#             files = {"file": (test_filename, f)}
#             upload_response = requests.post(
#                 upload_url, 
#                 files=files,
#                 headers={"Cookie": f"session={instructor_session}"}
#             )
        
#         log_response(upload_url, upload_response)
#         assert upload_response.status_code in [200, 201], "Failed to upload document"
        
#         chat_id = create_chat_session(student_session)
#         chatbot_url = f"{BASE_URL}/chatbot"
#         query_payload = {
#             "chat_id": chat_id,
#             "course_id": course_id,
#             "query": "What is the first thing to do in software testing ?"
#         }       
#         chatbot_response = requests.post(chatbot_url, json=query_payload, headers=auth_headers(student_session))
#         log_response(chatbot_url, chatbot_response)      
#         response_text = chatbot_response.json()["message"].lower()
        
#         assert "biology" in response_text
#         delete_url = f"{BASE_URL}/documents/{course_id}?filename={test_filename}"
#         requests.delete(delete_url, headers=auth_headers(instructor_session))
#         os.remove(test_filename)


# Chatbot Integration Testing
def test_ai_components_integration():
    test_content = """
    Software Testing is a crucial part of software development.
    It involves evaluating software to detect differences between expected and actual results.
    There are several types including unit testing, integration testing, and system testing.
    """
    test_filename = "testing_doc.txt"
    with open(test_filename, "w") as f:
        f.write(test_content)
    course_id = 1
    with open(test_filename, "rb") as f:
        files = {"file": (test_filename, f)}
        upload_response = requests.post(
            f"{BASE_URL}/documents/{course_id}", 
            files=files,
            headers={"Cookie": f"session={instructor_session}"}
        )
    
    assert upload_response.status_code in [200, 201], "Failed to upload document"
    chat_id = create_chat_session(student_session)
    chatbot_url = f"{BASE_URL}/chatbot"
    
    query_payload = {
        "chat_id": chat_id,
        "course_id": course_id,
        "query": "What is software testing and what are its types?"
    }
    
    response1 = requests.post(chatbot_url, json=query_payload, headers=auth_headers(student_session))
    assert response1.status_code == 200
    
    response_text = response1.json()["message"].lower()
    assert "software testing" in response_text
    assert any(test_type in response_text for test_type in ["unit testing", "integration testing", "system testing"])
    
    follow_up_payload = {
        "chat_id": chat_id,
        "course_id": course_id,
        "query": "Why is it important?"
    }
    
    response2 = requests.post(chatbot_url, json=follow_up_payload, headers=auth_headers(student_session))
    follow_up_text = response2.json()["message"].lower()
    
    assert any(term in follow_up_text for term in ["testing", "software", "quality"])
    
    delete_url = f"{BASE_URL}/documents/{course_id}?filename={test_filename}"
    requests.delete(delete_url, headers=auth_headers(instructor_session))
    os.remove(test_filename)