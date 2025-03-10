import { useAuthStore } from '@/stores/auth';
import { createRouter, createWebHistory } from 'vue-router';
import adminRoutes from './routes/admin';
import authRoutes from './routes/auth';
import commonRoutes from './routes/common';
import instructorRoutes from './routes/instructor';
import studentRoutes from './routes/student';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [...commonRoutes, ...authRoutes, ...adminRoutes, ...instructorRoutes, ...studentRoutes],
});

// Add navigation guards for auth and role checking
router.beforeEach((to, from, next) => {
    // Get auth state from store
    const authStore = useAuthStore();
    const userRole = authStore.isLoggedIn ? authStore.userRole : null;

    // If route requires authentication and user is not authenticated, redirect to login
    if (to.meta.requiresAuth && !authStore.isLoggedIn) {
        next({ name: 'auth-LoginView' });
        return;
    }

    // If route requires a specific role and user doesn't have it, redirect to home
    if (to.meta.role && to.meta.role !== userRole) {
        next({ name: 'home' });
        return;
    }

    // Otherwise proceed
    next();
});

export default router;
