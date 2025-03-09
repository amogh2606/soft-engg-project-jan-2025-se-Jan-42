import router from '@/router';

export function getRouteBasedOnRole(userRole) {
    switch (userRole) {
        case 'student':
            return '/student/courses';
        case 'instructor':
            return '/instructor/courses';
        case 'admin':
            return '/admin/courses';
        default:
            return '/';
    }
}

export function redirectBasedOnRole(userRole) {
    const route = getRouteBasedOnRole(userRole);
    router.push(route || '/');
}

export function redirectToLogin() {
    router.push('/auth/login');
}

export function redirectToHome() {
    router.push('/');
}
