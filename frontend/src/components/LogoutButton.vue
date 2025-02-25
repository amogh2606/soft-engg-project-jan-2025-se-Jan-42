<script setup>
import { useAuthStore } from '@/stores/auth';
import { push } from 'notivue';
import { useRouter } from 'vue-router';
import Button from '@/components/ui/buttons/Button.vue';

const authStore = useAuthStore();
const router = useRouter();

function logout() {
    authStore.logout();
    router.push('/auth/login');
    push.success({
        message: 'Logged out successfully',
    });
}
</script>

<template>
    <Button @click="logout" class="w-full" varient="outlineRed"> Logout </Button>
</template>
