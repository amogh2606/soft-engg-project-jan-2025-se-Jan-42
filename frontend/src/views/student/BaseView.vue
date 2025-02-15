<script setup>
import AttachmentIcon from '@/components/icons/AttachmentIcon.vue';
import BookIcon from '@/components/icons/BookIcon.vue';
import BookMarkIcon from '@/components/icons/BookmarkIcon.vue';
import ChatbotIcon from '@/components/icons/ChatbotIcon.vue';
import ChatIcon from '@/components/icons/ChatIcon.vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';
import EditIcon from '@/components/icons/EditIcon.vue';
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import SendIcon from '@/components/icons/SendIcon.vue';
import UserIcon from '@/components/icons/UserIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
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
    <div class="flex h-screen w-screen flex-col">
        <header class="flex flex-wrap items-center justify-between border-b bg-white px-4 py-2">
            <RouterLink to="/">
                <IITMLogoIcon class="h-12" />
            </RouterLink>
            <div class="flex space-x-2">
                <RouterLink to="/auth/login">
                    <Button varient="light" class="!rounded-full !p-1.5">
                        <UserIcon :is-solid="false" :with-border="false" class="h-6 w-full" />
                    </Button>
                </RouterLink>
            </div>
        </header>
        <div class="flex flex-1 overflow-y-hidden">
            <div class="flex h-full flex-col items-center gap-2 overflow-y-scroll border-e pt-2">
                <RouterLink
                    to="/student/courses"
                    class="flex w-full flex-col items-center justify-center p-2 hover:bg-gray-300"
                    :class="{ 'bg-gray-300': isActive('/student/courses') }"
                >
                    <BookIcon :is-solid="isActive('/student/courses')" class="h-8 w-auto" />
                    <span class="text-sm">Courses</span>
                </RouterLink>
                <RouterLink
                    to="/student/chats"
                    class="flex w-full flex-col items-center justify-center p-2 hover:bg-gray-300"
                    :class="{ 'bg-gray-300': isActive('/student/chats') }"
                >
                    <ChatIcon :is-solid="isActive('/student/chats')" class="h-8" />
                    <span class="text-sm">Chats</span>
                </RouterLink>
            </div>
            <slot name="left-slot"></slot>
            <slot name="right-slot"></slot>
        </div>

        <!-- Todo: Create Separate Component for Drawer -->
        <!-- drawer toggle -->
        <button class="absolute bottom-6 right-6" @click="toggleDrawer">
            <ChatbotIcon class="ai-btn h-12 w-auto" />
        </button>

        <!-- drawer component -->
        <div
            v-if="drawerOpen"
            class="absolute right-0 top-0 h-screen w-screen bg-black opacity-50"
            id="overlay"
        ></div>
        <div
            v-if="drawerOpen"
            class="absolute right-0 top-0 flex h-screen w-full flex-col bg-white sm:w-1/2 md:w-1/3"
            id="drawer"
        >
            <!-- header -->
            <div class="flex items-center justify-between border-b border-black bg-slate-200 p-2">
                <p class="text-lg">Chat Title Here ...</p>
                <div class="flex gap-2">
                    <button class="rounded border border-black p-1 hover:bg-gray-100">
                        <EditIcon class="h-6 w-auto" />
                    </button>
                    <button class="rounded border border-black p-1 hover:bg-gray-100">
                        <BookMarkIcon class="h-6 w-auto" />
                    </button>
                    <button
                        class="rounded border border-black p-1 hover:bg-gray-100"
                        @click="toggleDrawer"
                    >
                        <CrossIcon class="h-6 w-auto" />
                    </button>
                </div>
            </div>

            <!-- body -->
            <div class="flex h-full w-full flex-1 overflow-y-scroll">
                <div class="flex flex-1 flex-col items-center gap-2 overflow-y-scroll p-2">
                    <div class="ms-auto mt-auto flex w-4/5 rounded-md bg-blue-200 p-2">
                        <p>What is 2 + 2 ?</p>
                    </div>
                    <div class="me-auto flex w-4/5 rounded-md bg-green-200 p-2">
                        <p>
                            I can't give you the direct answer. But, you could get the answer by
                            solving the expression 6 - 2 = ?.
                        </p>
                    </div>
                    <div class="ms-auto flex w-4/5 rounded-md bg-blue-200 p-2">
                        <p>Got it ! Thanks :)</p>
                    </div>
                </div>
            </div>

            <!-- footer -->
            <div class="m-2 flex flex-col rounded-md border border-black">
                <textarea
                    type="text"
                    class="w-full resize-none rounded p-2 outline-none"
                    placeholder="Type a message ..."
                ></textarea>
                <div class="flex items-center justify-between p-2">
                    <button
                        class="flex items-center justify-center gap-1 rounded-md border p-1 px-2 hover:bg-gray-100"
                    >
                        <AttachmentIcon class="h-5 w-auto" />
                        <span class="text-sm">Context</span>
                    </button>
                    <button class="rounded-md border p-1.5 hover:bg-gray-100">
                        <SendIcon :is-solid="true" class="h-6 w-6" />
                    </button>
                </div>
            </div>
        </div>
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
