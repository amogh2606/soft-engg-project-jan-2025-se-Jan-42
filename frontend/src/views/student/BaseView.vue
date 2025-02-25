<script setup>
import ChatbotDrawer from '@/components/ChatbotDrawer.vue';
import BookIcon from '@/components/icons/BookIcon.vue';
import ChatbotIcon from '@/components/icons/ChatbotIcon.vue';
import ChatIcon from '@/components/icons/ChatIcon.vue';
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import UserDropdown from '@/components/ui/dropdown/UserDropdown.vue';
import BaseView from '@/views/BaseView.vue';
import { ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const drawerOpen = ref(false);
const toggleDrawer = () => {
    drawerOpen.value = !drawerOpen.value;
};

const isActive = (path) => {
    return useRoute().path === path;
};
</script>

<template>
    <BaseView>
        <div class="flex h-screen w-screen flex-col">
            <header class="flex flex-wrap items-center justify-between border-b bg-white px-4 py-2">
                <RouterLink to="/">
                    <IITMLogoIcon class="h-12" />
                </RouterLink>
                <div class="flex items-center space-x-2">
                    <UserDropdown />
                </div>
            </header>
            <div class="flex flex-1 overflow-y-hidden">
                <div class="flex h-full flex-col items-center overflow-y-scroll border-r bg-white">
                    <RouterLink
                        to="/student/courses"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive('/student/courses'),
                            'hover:bg-gray-300': isActive('/student/courses'),
                        }"
                    >
                        <BookIcon :is-solid="isActive('/student/courses')" class="h-8 w-auto" />
                        <span class="text-sm">Courses</span>
                    </RouterLink>
                    <RouterLink
                        to="/student/chats"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive('/student/chats'),
                            'hover:bg-gray-300': isActive('/student/chats'),
                        }"
                    >
                        <ChatIcon :is-solid="isActive('/student/chats')" class="h-8" />
                        <span class="text-sm">Chats</span>
                    </RouterLink>
                </div>
                <slot name="main-slot"></slot>
            </div>

            <!-- drawer toggle -->
            <button class="absolute bottom-6 right-6" @click="toggleDrawer">
                <ChatbotIcon class="ai-btn h-12 w-auto" />
            </button>
            <ChatbotDrawer :is-open="drawerOpen" :close-drawer="toggleDrawer" />
        </div>
    </BaseView>
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
