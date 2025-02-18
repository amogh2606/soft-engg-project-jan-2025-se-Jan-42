<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import router from '@/router';
import BaseView from '@/views/auth/BaseView.vue';
import { push } from 'notivue';
import { RouterLink } from 'vue-router';

function submit(event) {
    console.log('Login form submitted');

    // Prevent the form from submitting
    event.preventDefault();
    const userType = event.target.user.value;

    if (userType === 'student') {
        router.push('/student/courses');
    } else if (userType === 'instructor') {
        router.push('/instructor/faqs');
    } else if (userType === 'admin') {
        router.push('/admin/courses');
    }

    push.success({
        message: 'Login successful',
    });
}
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex h-full items-center justify-center">
                <div class="mx-2 w-full max-w-md rounded-lg border bg-white p-6 shadow-md">
                    <h2 class="mb-6 text-center text-2xl font-bold text-gray-800">Login</h2>
                    <form @submit.prevent="submit">
                        <div class="mb-4">
                            <label class="block text-gray-700" for="email">Email</label>
                            <input
                                type="email"
                                id="email"
                                name="email"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            />
                        </div>
                        <div class="mb-4">
                            <label class="block text-gray-700" for="password">Password</label>
                            <input
                                type="password"
                                id="password"
                                name="password"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            />
                        </div>

                        <!-- TODO: Remove it later -->
                        <!-- selection input for user selection -->
                        <div class="mb-4">
                            <label class="block text-gray-700" for="user">User</label>
                            <select
                                id="user"
                                name="user"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            >
                                <option value="student">Student</option>
                                <option value="instructor">Instructor</option>
                                <option value="admin">Admin</option>
                            </select>
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
