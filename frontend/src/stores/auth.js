import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')) || null,
    }),

    getters: {
        isLoggedIn() {
            return this.user !== null;
        },

        userRole() {
            return this.user?.roles?.at(0);
        },
    },

    actions: {
        setUser(user) {
            this.user = user;
            localStorage.setItem('user', JSON.stringify(user));
        },

        clearUser() {
            this.user = null;
            localStorage.removeItem('user');
        },
    },
});

