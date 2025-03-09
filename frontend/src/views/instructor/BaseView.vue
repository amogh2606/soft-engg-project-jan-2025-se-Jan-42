<script setup>
import ChatbotDrawer from '@/components/ChatbotDrawer.vue';
import FaqIcon from '@/components/icons/FaqIcon.vue';
import FeedbackIcon from '@/components/icons/FeedbackIcon.vue';
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import ChatIcon from '@/components/icons/ChatIcon.vue';
import StackIcon from '@/components/icons/StackIcon.vue';
import BookIcon from '@/components/icons/BookIcon.vue';
import DraggableChatbotButton from '@/components/ui/buttons/DraggableChatbotButton.vue';
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
                        to="/instructor/courses"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive('/instructor/courses'),
                            'hover:bg-gray-300': isActive('/instructor/courses'),
                        }"
                    >
                        <BookIcon :is-solid="isActive('/instructor/courses')" class="h-8 w-auto" />
                        <span class="text-sm">Courses</span>
                    </RouterLink>
                    <RouterLink
                        to="/instructor/faqs"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive('/instructor/faqs'),
                            'hover:bg-gray-300': isActive('/instructor/faqs'),
                        }"
                    >
                        <FaqIcon class="h-8 w-auto" :is-solid="isActive('/instructor/faqs')" />
                        <span class="text-sm">Faqs</span>
                    </RouterLink>
                    <RouterLink
                        to="/instructor/feedbacks"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive('/instructor/feedbacks'),
                            'hover:bg-gray-300': isActive('/instructor/feedbacks'),
                        }"
                    >
                        <FeedbackIcon
                            class="h-8 w-auto"
                            :is-solid="isActive('/instructor/feedbacks')"
                        />
                        <span class="text-sm">Feedback</span>
                    </RouterLink>
                    <RouterLink
                        to="/instructor/kstack"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive('/instructor/kstack'),
                            'hover:bg-gray-300': isActive('/instructor/kstack'),
                        }"
                    >
                        <StackIcon class="h-9 w-auto" :is-solid="isActive('/instructor/kstack')" />
                        <span class="text-sm">KStack</span>
                    </RouterLink>
                    <RouterLink
                        to="/instructor/chats"
                        class="flex w-full flex-col items-center justify-center p-2 transition-colors hover:bg-gray-100"
                        :class="{
                            'bg-gray-300': isActive('/instructor/chats'),
                            'hover:bg-gray-300': isActive('/instructor/chats'),
                        }"
                    >
                        <ChatIcon class="h-8 w-auto" :is-solid="isActive('/instructor/chats')" />
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
