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

