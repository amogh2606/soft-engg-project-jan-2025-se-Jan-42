import { client } from '@/api/client';

export const loginUser = (email, password) => {
    return client.post('/login', { email, password });
};

export const logoutUser = () => {
    return client.post('/logout');
};

export const getUser = () => {
    return client.get('/user');
};

export const getUserChats = () => {
    return client.get('/chats/user');
};

export const getAllChats = () => {
    return client.get('/chats/all');
};

export const getChatById = (id) => {
    return client.get(`/chats/${id}`);
};

export const getAllCourses = () => {
    return client.get('/courses/all');
};
