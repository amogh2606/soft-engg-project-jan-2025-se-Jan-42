<script setup>
import LogoComponent from '@/components/icons/LogoComponent.vue';
import Button from '@/components/ui/buttons/Button.vue';
import { RouterLink } from 'vue-router';
</script>
<template>
    <header class="flex flex-wrap items-center justify-between border-b px-4 py-2">
        <RouterLink to="/">
            <LogoComponent class="h-12" />
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
    <main class="p-4 text-center">
        <h1 class="text-2xl font-bold">Home Page</h1>
        <p class="mt-2">This is the public home page</p>
    </main>
</template>
