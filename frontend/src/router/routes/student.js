import StudentChatsView from '@/views/student/ChatsView.vue';
import StudentCoursesListView from '@/views/student/CoursesListView.vue';

export default [
    {
        path: '/student/courses',
        name: 'student-CoursesListView',
        component: StudentCoursesListView,
        meta: {
            requiresAuth: true,
            role: 'student',
        },
    },
    {
        path: '/student/chats',
        name: 'student-ChatsView',
        component: StudentChatsView,
        meta: {
            requiresAuth: true,
            role: 'student',
        },
    },
];
