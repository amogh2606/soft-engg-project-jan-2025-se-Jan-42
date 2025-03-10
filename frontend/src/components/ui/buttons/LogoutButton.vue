<script setup>
import { logoutUser } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { useAuthStore } from '@/stores/auth';
import { redirectToLogin } from '@/utils/routerHelper';
import { push } from 'notivue';

const { clearUser } = useAuthStore();

async function logout() {
    try {
        await logoutUser();
        clearUser();
        redirectToLogin();

        push.success({
            message: 'Logged out successfully',
        });
    } catch (error) {
        console.error(error);
        push.error({
            message: error.message || 'An unexpected error occurred during logout.',
        });
    }
}
</script>

<template>
    <Button @click="logout" class="w-full" varient="outlineRed">Logout</Button>
</template>
