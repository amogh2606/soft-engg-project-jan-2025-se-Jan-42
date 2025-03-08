import { client } from '@/api/client';

export const loginUser = (email, password) => {
    return client.post('/login', { email, password });
};

export const logoutUser = () => {
    return client.post('/logout');
};

export const registerUser = (name, email, password) => {
    return client.post('/user', { name, email, password });
};

export const getUser = () => {
    return client.get('/user');
};

export const getAllUsers = (role) => {
    return client.get(`/users?role=${role}`);
};

export const getUserChats = () => {
    return client.get('/chats/user');
};

export const getAllChats = () => {
    return client.get('/chats/all');
};

export const getChatById = (chatId) => {
    return client.get(`/chats/${chatId}`);
};

export const getAllCourses = () => {
    return client.get('/courses/all');
};

export const getCourseById = (courseId) => {
    return client.get(`/courses/${courseId}`);
};

export const addCourse = (name, description) => {
    return client.post('/courses', { name, description });
};

export const getKnowledgeStackByCourseId = (courseId) => {
    return client.get(`/documents/${courseId}`);
};

export const deleteDocumentFromKnowledgeStack = (courseId, documentName) => {
    return client.delete(`/documents/${courseId}?filename=${documentName}`);
};

export const uploadDocumentToKnowledgeStack = (courseId, formData) => {
    return client.post(`/documents/${courseId}`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
};

export const getFeedbacksByCourseId = (courseId) => {
    return client.get(`/feedback/${courseId}`);
};

export const getCourseEnrollments = (courseId) => {
    return client.get(`/enrollments/${courseId}`);
};

export const enrollUserInCourse = (userId, courseId) => {
    return client.post(`/courses/enroll`, { user_id: userId, course_id: courseId });
};

export const getVideoById = (videoId) => {
    return client.get(`/videos/${videoId}`);
};

export const getAssignmentById = (assignmentId) => {
    return client.get(`/assignments/${assignmentId}`);
};
