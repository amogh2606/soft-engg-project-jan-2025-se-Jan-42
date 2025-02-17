import { createRouter, createWebHistory } from 'vue-router';
import AdminChatsView from '../views/admin/ChatsView.vue';
import AdminCoursesListView from '../views/admin/CoursesListView.vue';
import AdminEnrollmentsView from '../views/admin/EnrollmentsView.vue';
import AdminKnowledgeStackView from '../views/admin/KnowledgeStackView.vue';
import LoginView from '../views/auth/LoginView.vue';
import SignupView from '../views/auth/SignupView.vue';
import CourseView from '../views/course/CourseView.vue';
import HomeView from '../views/HomeView.vue';
import InstructorFaqView from '../views/instructor/FaqView.vue';
import InstructorFeedbackView from '../views/instructor/FeedbackView.vue';
import InstructorKnowledgeStackView from '../views/instructor/KnowledgeStackView.vue';
import NotFoundView from '../views/NotFoundView.vue';
import StudentChatsView from '../views/student/ChatsView.vue';
import StudentCoursesListView from '../views/student/CoursesListView.vue';

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
            component: LoginView,
        },
        {
            path: '/auth/signup',
            name: 'auth-SignupView',
            component: SignupView,
        },
        {
            path: '/course/:id',
            name: 'course-CourseView',
            component: CourseView,
        },
        {
            path: '/student/courses',
            name: 'student-CoursesListView',
            component: StudentCoursesListView,
        },
        {
            path: '/student/chats',
            name: 'student-ChatsView',
            component: StudentChatsView,
        },
        {
            path: '/instructor/faqs',
            name: 'instructor-FaqView',
            component: InstructorFaqView,
        },
        {
            path: '/instructor/feedbacks',
            name: 'instructor-FeedbackView',
            component: InstructorFeedbackView,
        },
        {
            path: '/instructor/kstack',
            name: 'instructor-KnowledgeStackView',
            component: InstructorKnowledgeStackView,
        },
        {
            path: '/admin/courses',
            name: 'admin-CoursesListView',
            component: AdminCoursesListView,
        },
        {
            path: '/admin/kstack',
            name: 'admin-KnowledgeStackView',
            component: AdminKnowledgeStackView,
        },
        {
            path: '/admin/enrollments',
            name: 'admin-EnrollmentsView',
            component: AdminEnrollmentsView,
        },
        {
            path: '/admin/chats',
            name: 'admin-ChatsView',
            component: AdminChatsView,
        },
        {
            path: '/:pathMatch(.*)*',
            name: 'not-found',
            component: NotFoundView,
        },
    ],
});

export default router;
