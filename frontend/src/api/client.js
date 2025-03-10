import { useAuthStore } from '@/stores/auth';
import { redirectToLogin } from '@/utils/routerHelper';
import axios from 'axios';

export const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:5000/api';

export const client = axios.create({
    baseURL: BASE_URL,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    },
});

client.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response?.status === 401) {
            const { clearUser } = useAuthStore();
            clearUser();
            redirectToLogin();
        }
        return Promise.reject(error);
    },
);
