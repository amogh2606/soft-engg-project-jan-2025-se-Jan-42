<script setup>
import ChatbotDrawer from '@/components/ChatbotDrawer.vue';
import BookIcon from '@/components/icons/BookIcon.vue';
import ChatIcon from '@/components/icons/ChatIcon.vue';
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import DraggableChatbotButton from '@/components/ui/buttons/DraggableChatbotButton.vue';
import UserDropdown from '@/components/ui/dropdown/UserDropdown.vue';
import BaseView from '@/views/BaseView.vue';
import { ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';

const drawerOpen = ref(false);
const toggleDrawer = () => {
    drawerOpen.value = !drawerOpen.value;
};

const isActive = (paths) => {
    return paths.includes(useRoute().path);
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
                        to="/admin/courses"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive([
                                '/admin/courses',
                                '/admin/enrollments',
                                '/admin/kstack',
                            ]),
                            'hover:bg-gray-300': isActive([
                                '/admin/courses',
                                '/admin/enrollments',
                                '/admin/kstack',
                            ]),
                        }"
                    >
                        <BookIcon
                            :is-solid="
                                isActive(['/admin/courses', '/admin/enrollments', '/admin/kstack'])
                            "
                            class="h-8 w-auto"
                        />
                        <span class="text-sm">Courses</span>
                    </RouterLink>
                    <RouterLink
                        to="/admin/chats"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive(['/admin/chats']),
                            'hover:bg-gray-300': isActive(['/admin/chats']),
                        }"
                    >
                        <ChatIcon :is-solid="isActive(['/admin/chats'])" class="h-8" />
                        <span class="text-sm">Chats</span>
                    </RouterLink>
                </div>
                <slot name="main-slot"></slot>
            </div>

            <!-- Use the new draggable chatbot button component -->
            <DraggableChatbotButton :on-toggle="toggleDrawer" />
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
