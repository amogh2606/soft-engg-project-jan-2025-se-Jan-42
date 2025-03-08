import HomeView from '@/views/HomeView.vue';
import NotFoundView from '@/views/NotFoundView.vue';
import CourseView from '@/views/course/CourseView.vue';

export default [
    {
        path: '/',
        name: 'home',
        component: HomeView,
        meta: {
            requiresAuth: false,
        },
    },
    {
        // /course?course_id=1
        path: '/course',
        name: 'course-CourseView',
        component: CourseView,
        meta: {
            requiresAuth: true,
        },
        props: (route) => ({
            courseId: route.query.course_id,
        }),
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'not-found',
        component: NotFoundView,
        meta: {
            requiresAuth: false,
        },
    },
];
