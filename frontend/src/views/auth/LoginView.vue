<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import router from '@/router';
import { useAuthStore } from '@/stores/auth';
import BaseView from '@/views/auth/BaseView.vue';
import { push } from 'notivue';
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const route = useRoute();
const email = ref('');
const password = ref('');
const authStore = useAuthStore();

// Check if email was passed from signup page
onMounted(() => {
    if (route.query.email) {
        email.value = route.query.email;
    }
});

function submit(event) {
    // Prevent the form from submitting
    event.preventDefault();

    if (!email.value || !password.value) {
        push.error({
            message: 'Please enter an email and password',
        });
        return;
    }

    try {
        // Use the auth store to login
        const user = authStore.login(email.value, password.value);

        // Redirect based on user role
        if (user.role === 'student') {
            router.push('/student/courses');
        } else if (user.role === 'instructor') {
            router.push('/instructor/faqs');
        } else if (user.role === 'admin') {
            router.push('/admin/courses');
        }

        push.success({
            message: `Login successful as ${user.role}`,
        });
    } catch (error) {
        push.error({
            message: 'Login failed',
        });
    }
}
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex h-full items-center justify-center">
                <div class="mx-2 w-full max-w-md rounded-lg border bg-white p-6 shadow-md">
                    <h2 class="mb-6 text-center text-2xl font-bold text-gray-800">Login</h2>
                    <form @submit="submit">
                        <div class="mb-4">
                            <label class="block text-gray-700" for="email">Email</label>
                            <input
                                v-model="email"
                                type="email"
                                id="email"
                                name="email"
                                placeholder="Enter email (prefix determines role)"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
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
