import LoginView from '@/views/auth/LoginView.vue';
import SignupView from '@/views/auth/SignupView.vue';

export default [
    {
        path: '/auth/login',
        name: 'auth-LoginView',
        component: LoginView,
        meta: {
            requiresAuth: false,
        },
    },
    {
        path: '/auth/signup',
        name: 'auth-SignupView',
        component: SignupView,
        meta: {
            requiresAuth: false,
        },
    },
];
