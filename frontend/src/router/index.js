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
            path: '/course/:id',
            name: 'course-CourseView',
            component: () => import('../views/course/CourseView.vue'),
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
            path: '/instructor/faqs',
            name: 'instructor-FaqView',
            component: () => import('../views/instructor/FaqView.vue'),
        },
        {
            path: '/instructor/feedbacks',
            name: 'instructor-FeedbackView',
            component: () => import('../views/instructor/FeedbackView.vue'),
        },
        {
            path: '/instructor/kstack',
            name: 'instructor-KnowledgeStackView',
            component: () => import('../views/instructor/KnowledgeStackView.vue'),
        },
        {
            path: '/admin/courses',
            name: 'admin-CoursesListView',
            component: () => import('../views/admin/CoursesListView.vue'),
        },
        {
            path: '/admin/kstack',
            name: 'admin-KnowledgeStackView',
            component: () => import('../views/admin/KnowledgeStackView.vue'),
        },
        {
            path: '/admin/enrollments',
            name: 'admin-EnrollmentsView',
            component: () => import('../views/admin/EnrollmentsView.vue'),
        },
        {
            path: '/admin/chats',
            name: 'admin-ChatsView',
            component: () => import('../views/admin/ChatsView.vue'),
        }
    ],
});

export default router;
