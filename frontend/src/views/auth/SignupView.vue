<script setup>
import { registerUser } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import router from '@/router';
import BaseView from '@/views/auth/BaseView.vue';
import { push } from 'notivue';
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const name = ref('');
const email = ref('');
const password = ref('');

const validateForm = () => {
    if (!name.value || !email.value || !password.value) {
        return false;
    }
    return true;
};

function submit() {
    if (!validateForm()) {
        push.error('Please fill all fields !');
        return;
    }

    registerUser(name.value, email.value, password.value)
        .then((res) => {
            console.log('addInstructor', res);
            push.success('Signup successful !');

            // For now, just redirect to login with the email pre-filled
            router.push({
                path: '/auth/login',
                query: { email: email.value },
            });
        })
        .catch((err) => {
            if (err?.response?.status === 400) {
                push.error(err?.response?.data?.message || 'Failed to signup');
            } else {
                push.error('Failed to signup');
            }
        });
}
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex h-full items-center justify-center">
                <div class="mx-2 w-full max-w-md rounded-lg border bg-white p-6 shadow-md">
                    <h2 class="mb-6 text-center text-2xl font-bold text-gray-800">Signup</h2>
                    <form @submit.prevent="submit">
                        <div class="mb-4">
                            <label class="block text-gray-700" for="name">Name</label>
                            <input
                                v-model="name"
                                type="text"
                                id="name"
                                name="name"
                                required
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            />
                        </div>
                        <div class="mb-4">
                            <label class="block text-gray-700" for="email">Email</label>
                            <input
                                v-model="email"
                                type="email"
                                id="email"
                                name="email"
                                required
                                placeholder="Use prefix to determine role (admin@, instructor@, student@)"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            />
                            <p class="mt-1 text-xs text-gray-500">
                                Email prefix determines your role: admin@, instructor@, or any other
                                prefix for student
                            </p>
                        </div>
                        <div class="mb-4">
                            <label class="block text-gray-700" for="password">Password</label>
                            <input
                                v-model="password"
                                type="password"
                                id="password"
                                name="password"
                                required
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            />
                        </div>
                        <Button type="submit" class="w-full">Signup</Button>
                    </form>
                    <p class="mt-4 text-center text-sm">
                        Already have an account?
                        <RouterLink to="/auth/login" class="font-semibold underline"
                            >Login</RouterLink
                        >
                    </p>
                </div>
            </div>
        </template>
    </BaseView>
</template>
