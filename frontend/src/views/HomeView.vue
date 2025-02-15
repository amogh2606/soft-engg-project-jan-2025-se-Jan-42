<script setup>
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import { RouterLink } from 'vue-router';
</script>
<template>
    <header class="flex flex-wrap items-center justify-between border-b bg-white px-4 py-2">
        <RouterLink to="/">
            <IITMLogoIcon class="h-12" />
        </RouterLink>
        <div class="flex space-x-2">
            <RouterLink to="/auth/login">
                <Button varient="primary">Login</Button>
            </RouterLink>
            <RouterLink to="/auth/signup">
                <Button varient="primary">Signup</Button>
            </RouterLink>
        </div>
    </header>
    <main class="flex h-full flex-col items-center justify-center">
        <h1 class="text-2xl font-bold">Home Page</h1>
        <p class="mt-2">This is the public home page</p>
    </main>
</template>
