# User Management Tests

## Test Case 1: User Registration with Valid Data

**Description:** Verify that a new user can register with valid details.

**Endpoint:** `/user`

**Request Method:** POST

**Inputs:**
- JSON Body: 
  ```json
  {
      "email": "testing@example.com",
      "password": "password123",
      "name": "Tester Kumar"
  }

**Expected Output:**

- HTTP Status Code: 201
```json  
{"message": "Registered successfully"}
```

**Actual Output:**

- HTTP Status Code: 201
```json
{"message": "Registered successfully"}
```
Result: Passed

```python
def test_user_registration_valid():
    url = f"{BASE_URL}/user"
    payload = {
        "email": f"testing3@example.com",
        "password": "password123",
        "name": "Tester Kumar"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    log_response(url, response)
    assert response.status_code == 201
    assert response.json()["message"] == "Registered successfully"
```

## Test Case 2: User Registration with Weak Password

**Description:** Verify that registration fails when using a password shorter than six characters.

**Endpoint:** `/user`

**Request Method:** POST

**Inputs:**
- JSON Body: 
  ```json
  {
    "email": "weakpass@example.com",
    "password": "12345",
    "name": "Weak Password User"
  }

**Expected Output:**

- HTTP Status Code: 400
```json  
{"message": "Minimum password length is 6 characters"}
```

**Actual Output:**

- HTTP Status Code: 400
```json  
{"message": "Minimum password length is 6 characters"}
```
Result: Passed

```python
def test_user_registration_weak_password():
    url = f"{BASE_URL}/user"
    payload = {
        "email": "weakpass@example.com",
        "password": "12345",
        "name": "Weak Password User"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)    log_response(url, response)
    assert response.status_code == 400
```

## Test Case 3: Login with Valid Credentials

**Description:** Verify that a user can log in with valid credentials.

**Endpoint:** `/login`

**Request Method:** POST

**Inputs:**
- JSON Body: 
  ```json
    {
        "email": "testing@example.com",
        "password": "password123"
    }
    ```

**Expected Output:**

- HTTP Status Code: 200
```json  
{"message": "Logged in successfully"}
```

**Actual Output:**

- HTTP Status Code: 200
```json  
{"message": "Logged in successfully"}
```

Result: Passed

```python
def test_login_valid():
    logout_user(student_session)
    url = f"{BASE_URL}/login"
    payload = {
        "email": "testing@example.com",
        "password": "password123"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
    assert response.json()["message"] == "Logged in successfully"
```

## Test Case 4: Login with Invalid Password

**Description:** Verify that login fails when using an incorrect password.

**Endpoint:** `/login`

**Request Method:** POST

**Inputs:**
- JSON Body: 
  ```json
    {
        "email": "admin@example.com",
        "password": "wrongpassword"
    }
    ```

**Expected Output:**

- HTTP Status Code: 401
```json  
{"message": "Invalid credentials"}
```

**Actual Output:**

- HTTP Status Code: 401
```json  
{"message": "Invalid credentials"}
```

Result: Passed

```python
def test_login_invalid_password():
    url = f"{BASE_URL}/login"
    payload = {
        "email": admin_creds["email"],
        "password": "wrongpassword"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    log_response(url, response)
    assert response.status_code == 401
    assert response.json()["message"] == "Invalid credentials"
```

## Test Case 5: Login with Nonexistent Email

**Description:** Verify that login fails when using an email not registered in the system.

**Endpoint:** `/login`

**Request Method:** POST

**Inputs:**
- JSON Body: 
  ```json
    {
        "email": "nonexistent@example.com",
        "password": "password123"
    }
    ```

**Expected Output:**

- HTTP Status Code: 401
```json  
{"message": "Invalid credentials"}
```

**Actual Output:**

- HTTP Status Code: 401
```json  
{"message": "Invalid credentials"}
```

Result: Passed

```python
def test_login_nonexistent_email():
    url = f"{BASE_URL}/login"
    payload = {
        "email": "nonexistent@example.com",
        "password": "password123"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    log_response(url, response)
    assert response.status_code == 401
```

## Test Case 6: Fetch User Profile (Logged-In User)

**Description:** Verify that a logged-in user can fetch their profile details.

**Endpoint:** `/user`

**Request Method:** GET

**Headers:**
- Cookie: `Session=<valid_session_cookie>`
- Content-Type: `application/json`


**Expected Output:**

- HTTP Status Code: 200
```json  
{
    "id": <user_id>,
    "email": "<user_email>",
    "name": "<user_name>",
    "roles": "<user_roles>",
    "courses": "<user_courses>"
}
```

**Actual Output:**
- HTTP Status Code: 200
```json
{
  "id": 11,
  "email": "testing@example.com",
  "name": "Tester Kumar",
  "roles": [
    "student"
  ],
  "courses": []
}
```
Result: Passed

```python
def test_fetch_user():
    url = f"{BASE_URL}/user"
    headers = auth_headers(student_session)
    response = requests.get(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
    user_data = response.json()    
    assert user_data["email"] == student_creds["email"]
```

## Test Case 7: Update User Profile (Valid Data)

**Description:** Verify that a logged-in user can update their profile details (email and name).

**Endpoint:** `/user`

**Request Method:** PUT

**Inputs:**
- Headers:
```json
{"Cookie": "student_session", "Content-Type": "application/json"}
```
- JSON Body: 
  ```json
    {
        "email": "updated_email@example.com",
        "name": "Updated Name"
    }
    ```
**Expected Output**
- HTTP Status Code: 200
```json
{
    "message": "Updated successfully"
}
```
**Actual Output**
- HTTP Status Code: 200
```json
{
    "message": "Updated successfully"
}
```
Result: Passed

```python
def test_update_user_profile():
    url = f"{BASE_URL}/user"
    payload = {
        "email": "updated_email@example.com",
        "name": "Updated Name"
    }
    headers = auth_headers(student_session)
    response = requests.put(url, json=payload, headers=headers)
    log_response(url, response)   
    assert response.status_code == 200
    assert response.json()["message"] == "Updated successfully"
```

## Test Case 8: Delete a User (By admin)

**Description:** Verify that the API successfully deletes a user by user-ID.

**Endpoint:** `/user/<user_id>`

**Request Method:** DELETE

**Headers:**
  - Cookie: `session=<admin_session>`
  - Content-Type: `application/json`

**Expected Output**
- HTTP Status Code: 200
```json
{
    "message": "Deleted successfully"
}
```
**Actual Output**
- HTTP Status Code: 200
```json
{
    "message": "Deleted successfully"
}
```
Result: Passed

```python
def test_delete_user():
    user_id = 8
    url = f"{BASE_URL}/user/{user_id}"
    headers = auth_headers(admin_session)
    response = requests.delete(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
    assert response.json()["message"] == "Deleted successfully"
```
# Course Management Tests

## Test Case 1: Fetch All Courses

**Description:** Verify that the /courses/all endpoint returns a list of all available courses with correct details.

**Endpoint:** `/courses/all`

**Request Method:** GET

**Headers:**
- Cookie: `session=<admin_session> or <student_session>`
- Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
[
    {
        "id": 1,
        "name": "Software Engineering",
    }, ...
]
```
**Actual Output:**
- HTTP Status Code: 200
```json
[
    {
        "id": 1,
        "name": "Software Engineering",
    }, ...
]
```
Result: Passed

```python
def test_fetch_all_courses():
    url = f"{BASE_URL}/courses/all"
    headers = auth_headers(admin_session) 
    response = requests.get(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200, "Failed to fetch courses"
```
## Test Case 2: Enroll a user in a Course

**Description:** Verify that the API successfully enrolls a user into a course.

**Endpoint:** `/courses/enroll`

**Request Method:** POST

**Headers:**
- Cookie: `session=<admin_session>`
- Content-Type: `application/json`

**Input**
```json
{
    "course_id": 1,
    "user_id": 2
}

```
**Expected Output:**
- HTTP Status Code: 201
```json  
{"message": "Enrolled successfully"}
```
**Actual Output:**
- HTTP Status Code: 201
```json
{"message": "Enrolled successfully"}
```
Result: Passed

```python
def test_enroll_user_in_course():
    url = f"{BASE_URL}/courses/enroll"
    payload = {
        "course_id": 2,
        "user_id": 5
    }
    headers = auth_headers(admin_session)
    response = requests.post(url, json=payload, headers=headers)
    log_response(url, response)
    assert response.status_code == 201, "Failed to enroll user in course"
    assert response.json()["message"] == "Enrolled successfully"
```

## Test Case 3: Fetch Users Enrolled in a Course (Admin Only)

**Description:** Verify that the API endpoint retrieves all users enrolled in a specific course when accessed by an admin.

**Endpoint:** `/enrollments/<course_id>`

**Request Method:** GET

**Headers:**
- Cookie: `session=<admin_session>`
- Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
{
  "enrolled_users": [
    {
      "id": 5,
      "email": "testuser_1741845109@example.com",
      "name": "Tester Kumar",
      "roles": [
        "instructor"
      ],
      "courses": [
        {
          "id": 2,
          "name": "Software Testing"
        }
      ]
    }
  ]
}
```
**Actual Output:**
- HTTP Status Code: 201
```json
{
  "enrolled_users": [
    {
      "id": 5,
      "email": "testuser_1741845109@example.com",
      "name": "Tester Kumar",
      "roles": [
        "instructor"
      ],
      "courses": [
        {
          "id": 2,
          "name": "Software Testing"
        }
      ]
    }
  ]
}
```
Result: Passed

```python
def test_fetch_enrolled_users():
    course_id = 2
    url = f"{BASE_URL}/enrollments/{course_id}"
    headers = auth_headers(admin_session)
    response = requests.get(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200, f"Failed to fetch enrolled users for course {course_id}"
```
## Test Case 4: Assign Instructor to Multiple Courses

**Description:** Verify that an instructor cannot be assigned to more than one course.

**Endpoint:** `/courses/enroll`

**Request Method:** POST

**Headers:**
- Cookie: `session=<admin_session>`
- Content-Type: `application/json`

**Input:**
```json
{
    "course_id": 1,
    "user_id": 5
}
```

**Expected Output:**
- HTTP Status Code: 400
```json  
{"message": "Instructor already assigned to a course"}
```
**Actual Output:**
- HTTP Status Code: 201
```json
{ "message": "Instructor already assigned to a course" }
```
Result: Passed

```python
def test_assign_instructor_to_multiple_courses():
    enroll_url = f"{BASE_URL}/courses/enroll"
    payload_course_1 = {
        "course_id": 1,
        "user_id": 5
    }
    headers = auth_headers(admin_session)
    response_course_1 = requests.post(enroll_url, json=payload_course_1, headers=headers)
    log_response(enroll_url, response_course_1)
    assert response_course_1.status_code == 400
    assert response_course_1.json()["message"] == "Instructor already assigned to a course"
```
## Test Case 5: Validate Role-Based Access Control for Course Creation

**Description:** Non-admin users (e.g., instructors and students) are denied access to the course creation endpoint.

**Endpoint:** `/courses`

**Request Method:** POST

**Headers:**
- Cookie: `session=<instructor_session>`
- Content-Type: `application/json`

**Inputs:**
```json
{
    "name": "AI-SMPS",
    "description": "An AI course"
}
```

**Expected Output:**
- HTTP Status Code: 403
```json  
{"message": "You do not have permission to view this resource."}
```

**Actual Output:**
- HTTP Status Code: 403
```json  
{"message": "You do not have permission to view this resource."}
```
Result: Passed

```python
def test_access_for_course_creation():
    url = f"{BASE_URL}/courses"
    payload = {
        "name": "AI-SMPS",
        "description": "An AI course"
    }
    instructor_headers = auth_headers(instructor_session)
    instructor_response = requests.post(url, json=payload, headers=instructor_headers)
    log_response(url, instructor_response)
    assert instructor_response.json() == {
  "meta": {
    "code": 403
  },
  "response": {
    "errors": [
      "You do not have permission to view this resource."
    ]
  }
}
```
# Video Management Tests

## Test Case 1: Generate Video Summary

**Description:** Verify that the API successfully generates a summary for a video lecture using its transcript.

**Endpoint:** `/videos/<video_id>/summary`

**Request Method:** POST

**Headers:**
- Cookie: `session=<summary_session>`
- Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
{
    "video_url": "<video_url>",
    "summary": "<generated_summary>"
}

```
**Actual Output:**
- HTTP Status Code: 200
```json  
 {
    "video_url": "https://www.youtube.com/watch?v=hKm_rh1RTJQ",
    "summary": "This lecture introduces a software engineering course designed to..."
}

```
Result: Passed

```python
def test_generate_video_summary():
    video_id = 1
    url = f"{BASE_URL}/videos/{video_id}/summary"
    headers = auth_headers(student_session)
    response = requests.post(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
```

# Assignment Management Tests

## Test Case 1: Validate Assignment Retrieval (Authorized User)

**Description:** A logged-in user can retrieve assignment details only for courses they are enrolled in.

**Endpoint:** `/assignments/<assignment_id>`

**Input**

- ***Request Method:*** GET
- `{"assignment_id":2}`
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
{
  "id": 7,
  "course_id": 4,
  "week": 1,
  "due_date": "2025-12-31 00:00:00",
  "questions": [{
      "id": 31,
      "qno": 1,
      "type": "MCQ",
      "text": "Mark the appropriate response. Deepthi is not here. Could you please ----------",
      "option_1": "Speak Up",
      "option_2": "Hang Up",
      "option_3": "Hang On",
      "option_4": "Ring her later",
      "correct_option": 4
    },...]}
```
**Actual Output:**
- HTTP Status Code: 200
```json  
{
  "id": 7,
  "course_id": 4,
  "week": 1,
  "due_date": "2025-12-31 00:00:00",
  "questions": [{
      "id": 31,
      "qno": 1,
      "type": "MCQ",
      "text": "Mark the appropriate response. Deepthi is not here. Could you please ----------",
      "option_1": "Speak Up",
      "option_2": "Hang Up",
      "option_3": "Hang On",
      "option_4": "Ring her later",
      "correct_option": 4
    },...]}
```
Result: Passed

```python
def test_assignment_retrieval_auth_user():
    assignment_id = 7
    url = f"{BASE_URL}/assignments/{assignment_id}"
    headers = auth_headers(student_session)
    response = requests.get(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
```

# Chatbot Interaction Tests

## Test Case 1: Start a New Chat Session (Authorized User)

**Description:** Verify that a logged-in user can successfully start a new chat session.

**Endpoint:** `/chats`

**Input**
- ***Request Method:*** POST
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
{
  "id": 2,
  "user_id": 12,
  "title": "Untitled Chat",
  "created": "2025-03-13 16:45:59",
  "active": true,
  "bookmarked": false,
  "messages": []
}
```
**Actual Output:**
- HTTP Status Code: 200
```json  
{
  "id": 2,
  "user_id": 12,
  "title": "Untitled Chat",
  "created": "2025-03-13 16:45:59",
  "active": true,
  "bookmarked": false,
  "messages": []
}
```
Result: Passed

```python
def test_start_new_chat_session():
    url = f"{BASE_URL}/chats"
    headers = auth_headers(student_session)
    response = requests.post(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
```

## Test Case 2: Start a New Chat Session with an existing active chat session

**Description:** Verify that a logged-in user cannot start a new chat session without closing the previous one.

**Endpoint:** `/chats`

**Inputs:**
- ***Request Method:*** POST
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 400
```json  
{
  "id": 17,
  "active": "false"
}
{
  "id": 18,
  "active": "true"
}

```
**Actual Output:**
- HTTP Status Code: 400
```json  
{
  "id": 17,
  "active": "false"
}
{
  "id": 18,
  "active": "true"
}
```
Result: Passed

```python
def test_start_new_chat_with_existing_active_session():
    url = f"{BASE_URL}/chats"
    headers = auth_headers(student_session)
    response1 = requests.post(url, headers=headers)
    first_chat_id = response1.json()["id"]
    response2 = requests.post(url, headers=headers)
    second_chat_id = response2.json()["id"]
    get_url_first = f"{BASE_URL}/chats/{first_chat_id}"
    response_get_first = requests.get(get_url_first, headers=headers)
    log_response(get_url_first, response_get_first)    
    assert not response_get_first.json()["active"]
    get_url_second = f"{BASE_URL}/chats/{second_chat_id}"
    response_get_second = requests.get(get_url_second, headers=headers)
    log_response(get_url_second, response_get_second)
    assert response_get_second.json()["active"]
```

## Test Case 3: Send a Query to the Chatbot (Authorized User)

**Description:** Verify that the chatbot processes user queries and provides valid responses based on context or course-specific knowledge.

**Endpoint:** `/chatbot`

**Input**
- ***Request Method:*** POST
- ```json
  {
      "chat_id": 2,
      "query": "What is software engineering?"
  }
  ```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
 {
  "chat_id": 2,
  "timestamp": "2025-03-13 16:50:14",
  "message": "Software Engineering is a course in the BSc level of the BS in Data Science & Applications program by IIT Madras."
}
```
**Actual Output:**
- HTTP Status Code: 200
```json  
 {
  "chat_id": 2,
  "timestamp": "2025-03-13 16:50:14",
  "message": "Software Engineering is a course in the BSc level of the BS in Data Science & Applications program by IIT Madras."
}
```
Result: Passed

```python
def test_chatbot_interaction():
    chatbot_url = f"{BASE_URL}/chatbot"
    payload = {
        "chat_id": 2, # Must be active
        "query": "What is software engineering?"
    }
    headers = auth_headers(student_session)
    chatbot_response = requests.post(chatbot_url, json=payload, headers=headers)
    log_response(chatbot_url, chatbot_response)   
    assert chatbot_response.status_code == 200
```
## Test Case 4: Course Specific Query (Authorized User)

**Description:** Verify that the chatbot provides accurate and relevant responses to course-specific queries when a course_id is provided.

**Endpoint:** `/chatbot`

**Input**
- ***Request Method:*** POST
- ```json
  {
    "chat_id": 2,
    "course_id": 4,
    "query": "What topics are covered in this course?"
  }
  ```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
 {
  "chat_id": 2,
  "timestamp": "2025-03-13 17:51:32",
  "message": "This course covers basic English concepts, focusing on improving speaking, writing, reading, and listening skills. It also aims to help you understand how language works and how it relates to data, which can be useful for data science and computer programming."
}
```
**Actual Output:**
- HTTP Status Code: 200
```json  
{
  "chat_id": 2,
  "timestamp": "2025-03-13 17:51:32",
  "message": "This course covers basic English concepts, focusing on improving speaking, writing, reading, and listening skills. It also aims to help you understand how language works and how it relates to data, which can be useful for data science and computer programming."
}
```
Result: Passed

```python
def test_course_specific_query():
    chatbot_url = f"{BASE_URL}/chatbot"
    payload = {"chat_id": 2, "course_id": 3, "query": "What topics are covered in this course ?"}
    headers = auth_headers(student_session)
    response = requests.post(chatbot_url, json=payload, headers=headers)
    log_response(chatbot_url, response)
    assert response.status_code == 200
```

## Test Case 5: Chatbot Response to Ambiguous or Unclear Queries

**Description:** Verify that the chatbot can handle ambiguous or unclear queries gracefully by asking clarifying questions or guiding the user towards providing more specific input.

**Endpoint:** `/chatbot`

**Input**
- ***Request Method:*** POST
- ```json
  {
    "chat_id": 3,
    "query": "Can you explain me that topic ?"
  }
  ```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
   {
  "chat_id": 2,
  "timestamp": "2025-03-14 06:40:54",
  "message": "Clarify, which topic to explain you ?"
  }
```
**Actual Output:**
- HTTP Status Code: 200
```json  
  {
  "chat_id": 2,
  "timestamp": "2025-03-14 06:40:54",
  "message": "I am happy to help! Could you please specify which topic you would like me to explain?"
  }
```
Result: Passed

```python
def test_chatbot_response_to_ambiguous_query():
    chatbot_url = f"{BASE_URL}/chatbot"
    payload = {
        "chat_id": 2,
        "query": "Can you explain that topic ?"
    }
    headers = auth_headers(student_session)
    response = requests.post(chatbot_url, json=payload, headers=headers)
    log_response(chatbot_url, response)
    assert response.status_code == 200
    response_message = response.json()["message"].lower()
    assert any(phrase in response_message for phrase in [
        "clarify", 
        "more specific", 
        "please elaborate", 
        "which topic",
        "could you specify"
    ])
```

# Document Management Tests

## Test Case 1: Retrieve List of Uploaded Documents for Course (Admin or Instructor)

**Description:** Verify that admin or instructor can retrieve a list of all documents uploaded for a specific course.

**Endpoint:** `/documents/<course_id>`

**Input**
- ***Request Method:*** GET
- ***Headers:***
  - Cookie: `session=<admin_session> or <instructor_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
   {
  "collection": "course_2",
  "documents": [
    "1.1 Software Testing Motivation.txt",
    "1.2 Software Development Life Cycle.txt",
    ...
  ]
}
```
**Actual Output:**
- HTTP Status Code: 200
```json  
   {
  "collection": "course_2",
  "documents": [
    "1.1 Software Testing Motivation.txt",
    "1.2 Software Development Life Cycle.txt",
    ...
  ]
}
```
Result: Passed

```python
def test_retrieve_uploaded_documents_for_course():
    course_id = 2
    url = f"{BASE_URL}/documents/{course_id}"
    headers = auth_headers(admin_session)
    response = requests.get(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
```


# FAQs Management Tests

## Test Case 1: Validate FAQs Retrieval (Admin or Instructor)

**Description:** Verify that an admin or instructor can fetch the latest dynamically generated FAQs and that the response contains the correct structure and data.

**Endpoint:** `/faqs`

**Input**
- ***Request Method:*** GET
- ***Headers:***
  - Cookie: `session=<admin_session> or <instructor_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
   {
  "faqs": []
}
```
**Actual Output:**
- HTTP Status Code: 200
```json  
   {
  "faqs": []
}
```
Result: Passed

```python
def test_retrieve_faqs_with_auth():
    url = f"{BASE_URL}/faqs"
    headers = auth_headers(instructor_session)
    response = requests.get(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
```


# Feedback Management Tests

## Test Case 1: Submit Feedback for a Course (Student Role)

**Description:** Verify that a student can successfully submit feedback for a course they are enrolled in.

**Endpoint:** `/feedback/<course_id>`

**Input**
- ***Request Method:*** POST
```json
{
  "title": "Great course!",
  "text": "The lectures were very informative and engaging."
}
```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 201
```json  
   {
  "message": "Feedback submitted successfully"
}
```
**Actual Output:**
- HTTP Status Code: 201
```json  
   {
  "message": "Feedback submitted successfully"
}
```
Result: Passed

```python
def test_submit_feedback():
    course_id = 1
    url = f"{BASE_URL}/feedback/{course_id}"
    headers = auth_headers(student_session)
    payload = {
        "title": "Great course!",
        "text": "The lectures were very informative and engaging."
    }
    response = requests.post(url, json=payload, headers=headers)
    log_response(url, response)
    assert response.status_code == 201
    assert response.json()["message"] == "Feedback submitted successfully"
```

## Test Case 2: Retrieve Feedback for a Course (Instructor Role)

**Description:** Verify that an instructor can retrieve all feedback submitted by students for a course they are assigned to.

**Endpoint:** `/feedback/<course_id>`

**Input**
- ***Request Method:*** GET
- ***Headers:***
  - Cookie: `session=<instructor_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
   [
  {
    "id": 1,
    "course_id": 1,
    "created": "2025-03-14 08:52:13",
    "title": "Great course!",
    "text": "The lectures were very informative and engaging."
  }
]
```
**Actual Output:**
- HTTP Status Code: 200
```json  
   [
  {
    "id": 1,
    "course_id": 1,
    "created": "2025-03-14 08:52:13",
    "title": "Great course!",
    "text": "The lectures were very informative and engaging."
  }
]
```
Result: Passed

```python
def test_retrieve_feedback():
    course_id = 1
    url = f"{BASE_URL}/feedback/{course_id}"
    headers = auth_headers(instructor_session)
    response = requests.get(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
    feedback_list = response.json()
    assert isinstance(feedback_list, list)
```
## Test Case 3: Submit Feedback for Non-Enrolled Course (Student Role)

**Description:** Verify that a student cannot submit feedback for a course they are not enrolled in.

**Endpoint:** `/feedback/<course_id>`

**Input**
- ***Request Method:*** POST
```json
{
  "title": "Great course!",
  "text": "The lectures were very informative and engaging."
}
```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 400
```json  
   {
  "message": "Course not enrolled"
}
```
**Actual Output:**
- HTTP Status Code: 400
```json  
   {
  "message": "Course not enrolled"
}
```
Result: Passed

```python
def test_submit_feedback_non_enrolled_course():
    non_enrolled_course_id = 3
    url = f"{BASE_URL}/feedback/{non_enrolled_course_id}"
    headers = auth_headers(student_session)
    
    payload = {
        "title": "Great course!",
        "text": "The lectures were very informative and engaging."
    }
    response = requests.post(url, json=payload, headers=headers)
    log_response(url, response)
    assert response.status_code == 400
```

# Authentication & Authorization Tests

## Test Case 1: Logout Functionality

**Description:** Verify that a logged-in user can successfully log out and their session is invalidated.

**Endpoint:** `/logout`

**Input**
- ***Request Method:*** POST
- ***Headers:***
  - Cookie: `session=<student_session> or <instructor_session> or <admin_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
```json  
  {
    "message": "Logged out successfully"
}
```
**Actual Output:**
- HTTP Status Code: 200
```json  
  {
  "message": "Logged out successfully"
}
```
Result: Passed

```python
def test_logout():
    url = f"{BASE_URL}/logout" 
    headers = auth_headers(student_session) 
    response = requests.post(url, headers=headers)
    log_response(url, response)
    assert response.status_code == 200
    assert response.json()["message"] == "Logged out successfully"
```
# AI Component Tests

## Test Case 1: Chatbot Response Quality Assessment

**Description:** Verify that the chatbot provides informative and relevant responses with appropriate domain terminology.

**Endpoint:** `/chatbot`

**Input**
- ***Request Method:*** POST
```json
  {
    "chat_id": 1,
    "query": "What is the software development life cycle?"
  }
```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
- Response contains key SDLC terminology and comprehensive explanation.

**Actual Output:**
- HTTP Status Code: 200
```json  
  {
  "chat_id": 1,
  "timestamp": "2025-03-18 11:30:23",
  "message": "The Software Development Life Cycle (SDLC) is a systematic process for planning, creating, testing, and deploying software. It typically includes phases such as requirements gathering, design, implementation, testing, deployment, and maintenance. Different methodologies like Waterfall, Agile, and DevOps implement the SDLC in various ways to manage software development efficiently."
  }
```
Result: Passed

```python
def test_chatbot_response_quality():
    chat_id = create_chat_session(student_session)   
    chatbot_url = f"{BASE_URL}/chatbot"
    query_payload = {
        "chat_id": chat_id,
        "query": "What is the software development life cycle?"
    }
    response = requests.post(chatbot_url, json=query_payload, headers=auth_headers(student_session))
    log_response(chatbot_url, response)   
    assert response.status_code == 200
    response_text = response.json()["message"].lower()
    sdlc_terms = ["requirement", "design", "development", "testing", "deployment", "maintenance"]
    matches = [term for term in sdlc_terms if term in response_text]  
    assert len(matches) >= 3
```
## Test Case 2: Chatbot Context Awareness

**Description:** Test if chatbot maintains context across multiple messages in a conversation.

**Endpoint:** `/chatbot`

**Input**
- ***Request Method:*** POST
```json
  {
    "chat_id": 1,
    "query": "What is software testing?"
  }
  {
  "chat_id": 1,
  "query": "What are its different types?"
  }
```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
- Response mentions various testing types while maintaining context about software testing.

**Actual Output:**
- HTTP Status Code: 200
```json  
  {
    "chat_id": 1,
    "timestamp": "2025-03-18 11:32:15",
    "message": "Software testing can be categorized into several types, including: 1) Unit Testing - testing individual components, 2) Integration Testing - testing interactions between components, 3) System Testing - testing the entire application, 4) Acceptance Testing - verifying the software meets requirements, 5) Black Box Testing - focusing on inputs and outputs without internal knowledge, and 6) White Box Testing - examining the internal structure and logic."
  }
```
Result: Passed

```python
def test_chatbot_context_awareness():
    chat_id = create_chat_session(student_session)  
    chatbot_url = f"{BASE_URL}/chatbot"
    first_query = {
        "chat_id": chat_id,
        "query": "What is software testing?"
    }
    requests.post(chatbot_url, json=first_query, headers=auth_headers(student_session))
    follow_up_query = {
        "chat_id": chat_id,
        "query": "What are its different types?"
    }
    follow_up_response = requests.post(chatbot_url, json=follow_up_query, headers=auth_headers(student_session))
    log_response(f"{chatbot_url} (follow-up)", follow_up_response)   
    assert follow_up_response.status_code == 200
    response_text = follow_up_response.json()["message"].lower()
    testing_types = ["unit", "integration", "system", "acceptance", "black box", "white box"]
    matches = [test_type for test_type in testing_types if test_type in response_text]    
    assert len(matches) >= 2
    assert "software testing" in response_text or "testing" in response_text
```
## Test Case 3: Assignment Help Quality

**Description:** Verify that assignment help provides useful hints without revealing answers.

**Endpoint:** `/assignments/help`

**Input**
- ***Request Method:*** POST
```json
  {
  "question_id": 1,
  "assignment_id": 1,
  "course_id": 1
  }
```
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
- Response provides helpful hints without revealing the correct answer

**Actual Output:**
- HTTP Status Code: 200
```json  
  {
  "chat_id": 5,
  "timestamp": "2025-03-18 11:35:47",
  "message": "When considering this question about software development processes, think about the advantages of identifying errors early in the development lifecycle. Consider how catching issues during the requirements or design phase compares cost-wise to finding them after the software has been deployed. Remember that the correct answer relates to cost-effectiveness and resource allocation."
  }
```
Result: Passed

```python
def test_assignment_help_quality():
    assignment_id = 1
    url = f"{BASE_URL}/assignments/{assignment_id}"
    assignment_response = requests.get(url, headers=auth_headers(student_session))   
    if assignment_response.status_code != 200 or not assignment_response.json().get("questions"):
        pytest.skip("No questions available for testing")  
    question = assignment_response.json()["questions"][0]
    question_id = question["id"]
    correct_option = question["correct_option"]
    course_id = assignment_response.json()["course_id"]
    help_url = f"{BASE_URL}/assignments/help"
    payload = {
        "question_id": question_id,
        "assignment_id": assignment_id,
        "course_id": course_id
    }   
    help_response = requests.post(help_url, json=payload, headers=auth_headers(student_session))
    log_response(help_url, help_response)    
    assert help_response.status_code == 200
    hint_text = help_response.json()["message"].lower()
    assert len(hint_text) > 50
    correct_text = question[f"option_{correct_option}"].lower()
    assert correct_text not in hint_text
    assert str(correct_option) not in hint_text
```

## Test Case 4: Video Summary Quality

**Description:** Test that generated video summaries provide informative and coherent content.

**Endpoint:** `/videos/<video_id>/summary`

**Input**
- ***Request Method:*** POST
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
- Response includes a coherent, well-structured summary of the video content.

**Actual Output:**
- HTTP Status Code: 200
```json  
  {
  "video_url": "https://www.youtube.com/watch?v=hKm_rh1RTJQ",
  "summary": "This lecture introduces the fundamental concepts of Software Engineering. It begins by covering the historical context of software development, from early programming paradigms to modern methodologies. The speaker emphasizes the importance of structured approaches to software development, discussing key concepts such as requirements engineering, software design principles, and quality assurance. The lecture also touches on project management aspects, highlighting how proper engineering principles help manage complexity in large software systems. The importance of documentation, testing, and maintenance is stressed throughout, with practical examples to illustrate these concepts."
  }
```
Result: Passed

```python
def test_video_summary_quality():
    videos_url = f"{BASE_URL}/videos/all"
    videos_response = requests.get(videos_url, headers=auth_headers(admin_session))   
    if videos_response.status_code != 200 or not videos_response.json():
        pytest.skip("No videos available for testing")   
    video_id = videos_response.json()[0]["id"]
    summary_url = f"{BASE_URL}/videos/{video_id}/summary"   
    response = requests.post(summary_url, headers=auth_headers(student_session))
    log_response(summary_url, response)   
    assert response.status_code == 200
    summary = response.json()["summary"]
    assert len(summary) > 100
    assert len(summary.split(".")) > 3, "Summary has too few sentences"   
    low_quality_indicators = ["i don't know", "i'm not sure", "i cannot", "as an ai"]
    for indicator in low_quality_indicators:
        assert indicator not in summary.lower()
```

## Test Case 5: Quiz Generation Quality

**Description:** Verify that generated quizzes have proper format and relevant content.

**Endpoint:** `/videos/<video_id>/quiz`

**Input**
- ***Request Method:*** POST
- ***Headers:***
  - Cookie: `session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
- Response includes properly formatted multiple-choice questions related to video content.

**Actual Output:**
- HTTP Status Code: 200
```json  
  {
  "video_url": "https://www.youtube.com/watch?v=hKm_rh1RTJQ",
  "quiz": "1. What is the primary goal of software engineering?\nA) Writing code quickly\nB) Developing maintainable, reliable software systems\nC) Reducing the need for testing\nD) Eliminating the need for documentation\n\n2. Which of the following is NOT a phase in the software development lifecycle?\nA) Requirements gathering\nB) Implementation\nC) Marketing\nD) Maintenance\n\n3. What problem does version control help solve in software development?\nA) Code execution speed\nB) Collaboration and code history tracking\nC) Automatic bug fixes\nD) User interface design\n\n4. Which testing approach examines internal code structure?\nA) Black box testing\nB) White box testing\nC) Grey box testing\nD) Random testing\n\n5. What principle suggests that software modules should have only one reason to change?\nA) Dependency Inversion\nB) Interface Segregation\nC) Single Responsibility\nD) Open/Closed"
  }
```
Result: Passed

```python
def test_quiz_generation_quality():
    videos_url = f"{BASE_URL}/videos/all"
    videos_response = requests.get(videos_url, headers=auth_headers(admin_session))
    if videos_response.status_code != 200 or not videos_response.json():
        pytest.skip("No videos available for testing")
    video_id = videos_response.json()[0]["id"]
    quiz_url = f"{BASE_URL}/videos/{video_id}/quiz"
    response = requests.post(quiz_url, headers=auth_headers(student_session))
    log_response(quiz_url, response) 
    assert response.status_code == 200
    quiz = response.json()["quiz"]
    option_patterns = ["A)", "B)", "C)", "D)", "1.", "2.", "3.", "4."]
    has_options = any(pattern in quiz for pattern in option_patterns)
    assert has_options, "Quiz doesn't have proper option format"
    question_count = 0
    lines = quiz.split('\n')
    for i, line in enumerate(lines):
        if any(f"{num}." in line or f"{num})" in line for num in range(1, 10)):
            question_count += 1   
    assert question_count >= 3
```

## Test Case 6: Document Upload and Retrieval Influence

**Description:** Verify that uploaded documents influence chatbot responses with relevant knowledge.

**Endpoint:** `/documents/<course_id> (Upload) and /chatbot (Query)`

**Input**
- ***Request Method:*** POST
- File upload with test document containing specific content.
```json
  {
    "chat_id": 1,
    "course_id": 1,
    "query": "What are black box and white box testing?"
  }
```
- ***Headers:***
  - Cookie: `session=<instructor_session> and session=<student_session>`
  - Content-Type: `application/json`

**Expected Output:**
- HTTP Status Code: 200
- Response includes information from the uploaded document.

**Actual Output:**
- HTTP Status Code: 200
```json  
  {
  "chat_id": 1,
  "timestamp": "2025-03-18 11:42:10",
  "message": "Black box testing examines functionality without looking at internal code. It focuses on inputs and outputs, treating the system as a 'black box' whose internal workings are not considered. White box testing examines the internal structure of the software, looking at code paths, conditions, and implementation details to ensure proper functionality. Both approaches have their places in a comprehensive testing strategy."
  }
```
Result: Passed

```python
def test_document_upload_and_influence_responses():
    test_content = """
    This is a test document about software testing techniques.
    Black box testing examines functionality without looking at internal code.
    White box testing examines the internal structure of the software.
    """
    test_filename = "test_document.txt"
    with open(test_filename, "w") as f:
        f.write(test_content)
    course_id = 1
    upload_url = f"{BASE_URL}/documents/{course_id}"  
    with open(test_filename, "rb") as f:
        files = {"file": (test_filename, f)}
        upload_response = requests.post(
            upload_url, 
            files=files,
            headers={"Cookie": f"session={instructor_session}"}
        ) 
    log_response(upload_url, upload_response)
    if upload_response.status_code not in [200, 201]:
        pytest.skip("Failed to upload document")
    chat_id = create_chat_session(student_session)
    chatbot_url = f"{BASE_URL}/chatbot"
    query_payload = {
        "chat_id": chat_id,
        "course_id": course_id,
        "query": "What are black box and white box testing?"
    } 
    chatbot_response = requests.post(chatbot_url, json=query_payload, headers=auth_headers(student_session))
    log_response(chatbot_url, chatbot_response)  
    response_text = chatbot_response.json()["message"].lower()  
    assert "black box" in response_text
    assert "white box" in response_text
```

# AI Components Integration Test

**Description:** Verify that multiple AI components work together seamlessly, including document processing, chatbot context awareness, and follow-up question handling.

**Endpoint:** `/documents/<course_id> (Upload) and /chatbot (Query)`
**Request Method:** POST
**Inputs**
- File upload with test document containing specific content. Then, a question with a follow-up question.

- ***Headers:***
  - Cookie: `session=<instructor_session> and session=<student_session>`
  - Content-Type: `application/json and multipart/form-data`

**Expected Output:**
- HTTP Status Code: 200

**Actual Output:**
- HTTP Status Code: 200

Result: Passed

```python
def test_ai_components_integration():
    test_filename = "testing_doc.txt"
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
```