import InstructorCoursesListView from '@/views/instructor/CoursesListView.vue';
import InstructorFaqView from '@/views/instructor/FaqView.vue';
import InstructorFeedbackView from '@/views/instructor/FeedbackView.vue';
import InstructorKnowledgeStackView from '@/views/instructor/KnowledgeStackView.vue';
import InstructorChatsView from '@/views/instructor/ChatsView.vue';

export default [
    {
        path: '/instructor/faqs',
        name: 'instructor-FaqView',
        component: InstructorFaqView,
        meta: {
            requiresAuth: true,
            role: 'instructor',
        },
    },
    {
        path: '/instructor/feedbacks',
        name: 'instructor-FeedbackView',
        component: InstructorFeedbackView,
        meta: {
            requiresAuth: true,
            role: 'instructor',
        },
    },
    {
        path: '/instructor/kstack',
        name: 'instructor-KnowledgeStackView',
        component: InstructorKnowledgeStackView,
        meta: {
            requiresAuth: true,
            role: 'instructor',
        },
    },
    {
        path: '/instructor/courses',
        name: 'instructor-CoursesListView',
        component: InstructorCoursesListView,
        meta: {
            requiresAuth: true,
            role: 'instructor',
        },
    },
    {
        path: '/instructor/chats',
        name: 'instructor-ChatsView',
        component: InstructorChatsView,
        meta: {
            requiresAuth: true,
            role: 'instructor',
        },
    },
];
