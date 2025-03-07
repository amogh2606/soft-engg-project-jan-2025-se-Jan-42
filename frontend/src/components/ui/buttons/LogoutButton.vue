<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import { performLogout } from '@/services/authService';
import { useAuthStore } from '@/stores/auth';
import { redirectToLogin } from '@/utils/routerHelper';
import { push } from 'notivue';

const authStore = useAuthStore();

async function logout() {
    await performLogout();
    authStore.clearUser();

    redirectToLogin();
    push.success({
        message: 'Logged out successfully',
    });
}
</script>

<template>
    <Button @click="logout" class="w-full" varient="outlineRed"> Logout </Button>
</template>
