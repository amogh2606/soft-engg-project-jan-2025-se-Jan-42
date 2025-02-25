import AdminChatsView from '@/views/admin/ChatsView.vue';
import AdminCoursesListView from '@/views/admin/CoursesListView.vue';
import AdminEnrollmentsView from '@/views/admin/EnrollmentsView.vue';
import AdminKnowledgeStackView from '@/views/admin/KnowledgeStackView.vue';

export default [
    {
        path: '/admin/courses',
        name: 'admin-CoursesListView',
        component: AdminCoursesListView,
        meta: {
            requiresAuth: true,
            role: 'admin',
        },
    },
    {
        path: '/admin/kstack',
        name: 'admin-KnowledgeStackView',
        component: AdminKnowledgeStackView,
        meta: {
            requiresAuth: true,
            role: 'admin',
        },
    },
    {
        path: '/admin/enrollments',
        name: 'admin-EnrollmentsView',
        component: AdminEnrollmentsView,
        meta: {
            requiresAuth: true,
            role: 'admin',
        },
    },
    {
        path: '/admin/chats',
        name: 'admin-ChatsView',
        component: AdminChatsView,
        meta: {
            requiresAuth: true,
            role: 'admin',
        },
    },
];
