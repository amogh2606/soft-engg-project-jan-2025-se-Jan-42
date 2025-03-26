<script setup>
import { getUser, loginUser } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { useAuthStore } from '@/stores/auth';
import { redirectBasedOnRole } from '@/utils/routerHelper';
import BaseView from '@/views/auth/BaseView.vue';
import { push } from 'notivue';
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const route = useRoute();
const email = ref('');
const password = ref('password');
const authStore = useAuthStore();

// Check if email was passed from signup page
onMounted(() => {
    if (route.query.email) {
        email.value = route.query.email;
    }
});

const validateLoginForm = () => {
    if (!email.value || !password.value) {
        throw new Error('Please enter an email and password');
    }
};

const submit = async (event) => {
    event.preventDefault();


    try {
        validateLoginForm();

        await loginUser(email.value, password.value);
        const userResponse = await getUser();

        authStore.setUser(userResponse.data);
        push.success({ message: `Login successful as ${authStore.userRole}` });
        redirectBasedOnRole(authStore.userRole);
    } catch (error) {
        if (error.message === 'Already logged in') {
            return redirectBasedOnRole(authStore.userRole);
        }

        const errorMessage =
            error.response?.data?.message ||
            error.message ||
            'An unexpected error occurred during login.';
        push.error({ message: errorMessage });
    }
};
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex h-full items-center justify-center">
                <div class="mx-2 w-full max-w-md rounded-lg border bg-white p-6 shadow-md">
                    <h2 class="mb-6 text-center text-2xl font-bold text-gray-800">Login</h2>
                    <form @submit="submit">
                        <div class="mb-4">
                            <datalist id="email-prefix">
                                <option value="admin@example.com">Admin</option>
                                <option value="instructor@example.com">Instructor</option>
                                <option value="student@example.com">Student</option>
                            </datalist>
                            <label class="block text-gray-700" for="email">Email</label>
                            <input
                                v-model="email"
                                type="email"
                                id="email"
                                name="email"
                                placeholder="Enter email (prefix determines role)"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                                list="email-prefix"
                                autocomplete="off"
                            />
                            <p class="mt-1 text-xs text-gray-500">
                                Hint: Use "admin@example.com", "instructor@example.com", or
                                "student@example.com"
                            </p>
                        </div>
                        <div class="mb-4">
                            <label class="block text-gray-700" for="password">Password</label>
                            <input
                                v-model="password"
                                type="password"
                                id="password"
                                name="password"
                                placeholder="Enter any password"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            />
                        </div>
                        <Button type="submit" class="w-full">Login</Button>
                    </form>
                    <p class="mt-4 text-center text-sm">
                        Don't have an account?
                        <RouterLink to="/auth/signup" class="font-semibold underline"
                            >Sign up</RouterLink
                        >
                    </p>
                </div>
            </div>
        </template>
    </BaseView>
</template>

<style scoped>
input::-webkit-calendar-picker-indicator {
    opacity: 0;
}
</style>
