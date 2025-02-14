<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import router from '@/router';
import BaseView from '@/views/auth/BaseView.vue';
import { RouterLink } from 'vue-router';

function submit() {
    console.log('Signup form submitted');
    router.push('/auth/login');
}
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex h-full items-center justify-center">
                <div class="w-full max-w-md rounded bg-white p-6 shadow">
                    <h2 class="mb-6 text-center text-2xl font-bold text-gray-800">Signup</h2>
                    <form @submit.prevent="submit">
                        <div class="mb-4">
                            <label class="block text-gray-700" for="name">Name</label>
                            <input
                                type="text"
                                id="name"
                                name="name"
                                class="mt-2 w-full rounded border border-gray-400 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-gray-400"
                            />
                        </div>
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
