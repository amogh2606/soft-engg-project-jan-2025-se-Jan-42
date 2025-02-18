<script setup>
import ChatbotDrawer from '@/components/ChatbotDrawer.vue';
import ChatbotIcon from '@/components/icons/ChatbotIcon.vue';
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import ModulesIcon from '@/components/icons/ModulesIcon.vue';
import UserIcon from '@/components/icons/UserIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const drawerOpen = ref(false);
const toggleDrawer = () => {
    drawerOpen.value = !drawerOpen.value;
};
const showWeeklyIndex = ref(true);
</script>
<template>
    <div class="flex h-screen w-screen flex-col">
        <header class="flex flex-wrap items-center justify-between border-b bg-white px-4 py-2">
            <RouterLink to="/">
                <IITMLogoIcon class="me-6 h-12" />
            </RouterLink>
            <p class="me-auto rounded border bg-gray-50 p-2 font-semibold">
                Jan 2025 - Software Engineering
            </p>
            <div class="flex space-x-2">
                <RouterLink to="/auth/login">
                    <Button varient="light" class="!rounded-full !p-1.5">
                        <UserIcon :is-solid="false" :with-border="false" class="h-6 w-full" />
                    </Button>
                </RouterLink>
            </div>
        </header>

        <div class="flex flex-1 overflow-y-hidden">
            <div class="flex h-full flex-col items-center overflow-y-scroll border-r bg-white">
                <button
                    @click="showWeeklyIndex = !showWeeklyIndex"
                    class="flex w-full flex-col items-center justify-center bg-gray-300 p-2 transition-colors hover:bg-gray-300"
                >
                    <ModulesIcon class="h-8 w-full" />
                    <span class="text-sm">Modules</span>
                </button>
            </div>
            <slot name="main-slot" :showWeeklyIndex="showWeeklyIndex" />
        </div>

        <!-- drawer toggle -->
        <button class="absolute bottom-6 right-6" @click="toggleDrawer">
            <ChatbotIcon class="ai-btn h-12 w-auto" />
        </button>
        <ChatbotDrawer :is-open="drawerOpen" :close-drawer="toggleDrawer" />
    </div>
</template>

<style scoped>
.ai-btn {
    filter: drop-shadow(2px 4px 4px black);
    transition: transform 0.2s;
}
.ai-btn:hover {
    transform: scale(1.1);
}
</style>
