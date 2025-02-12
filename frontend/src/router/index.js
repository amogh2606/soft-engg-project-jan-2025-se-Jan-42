import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/auth/login',
            name: 'auth-LoginView',
            component: () => import('../views/auth/LoginView.vue'),
        },
        {
            path: '/auth/signup',
            name: 'auth-SignupView',
            component: () => import('../views/auth/SignupView.vue'),
        },
        {
            path: '/student/courses',
            name: 'student-CoursesListView',
            component: () => import('../views/student/CoursesListView.vue'),
        },
        {
            path: '/student/chats',
            name: 'student-ChatsView',
            component: () => import('../views/student/ChatsView.vue'),
        },
        {
            path: '/course/:id',
            name: 'course-CourseView',
            component: () => import('../views/course/CourseView.vue'),
        }
    ],
});

export default router;
