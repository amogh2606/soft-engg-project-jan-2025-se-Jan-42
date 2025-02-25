import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')) || null,
        isAuthenticated: localStorage.getItem('user') !== null,
    }),

    actions: {
        login(email, password) {
            // Dummy login logic - in a real app, this would call an API
            let user = null;

            // Simulate different user roles based on email prefix
            if (email.startsWith('admin')) {
                user = { id: 1, email, name: 'Admin User', role: 'admin' };
            } else if (email.startsWith('instructor')) {
                user = { id: 2, email, name: 'Instructor User', role: 'instructor' };
            } else {
                user = { id: 3, email, name: 'Student User', role: 'student' };
            }

            // Store user in localStorage
            localStorage.setItem('user', JSON.stringify(user));

            // Update state
            this.user = user;
            this.isAuthenticated = true;

            return user;
        },

        logout() {
            // Clear user from localStorage
            localStorage.removeItem('user');

            // Update state
            this.user = null;
            this.isAuthenticated = false;
        },

        getUser() {
            return this.user;
        },

        isLoggedIn() {
            return this.isAuthenticated;
        },
    },
});
