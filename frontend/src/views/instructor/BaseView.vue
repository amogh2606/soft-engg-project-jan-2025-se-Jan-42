<script setup>
import LogoComponent from '@/components/icons/LogoComponent.vue';
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
        <header class="flex flex-wrap items-center justify-between border-b px-4 py-2">
            <RouterLink to="/">
                <LogoComponent class="h-12" />
            </RouterLink>
            <div class="flex space-x-2">
                <RouterLink to="/auth/login">
                    <img
                        src="../../assets/images/profile-user.png"
                        alt="profile-user.png"
                        class="h-7 hover:opacity-70"
                    />
                </RouterLink>
            </div>
        </header>
        <div class="flex flex-1 overflow-y-hidden">
            <div class="flex h-full flex-col items-center gap-2 overflow-y-scroll border-e pt-2">
                <RouterLink
                    to="/instructor/faqs"
                    class="flex w-full flex-col items-center justify-center p-2 hover:bg-gray-300"
                    :class="{ 'bg-gray-300': isActive('/instructor/faqs') }"
                >
                    <img src="../../assets/images/faq.svg" alt="faq.svg" class="h-8" />
                    <span class="text-sm">Faqs</span>
                </RouterLink>
                <RouterLink
                    to="/instructor/feedbacks"
                    class="flex w-full flex-col items-center justify-center p-2 hover:bg-gray-300"
                    :class="{ 'bg-gray-300': isActive('/instructor/feedbacks') }"
                >
                    <img src="../../assets/images/feedback.svg" alt="feedback.svg" class="h-8" />
                    <span class="text-sm">Feedback</span>
                </RouterLink>
                <RouterLink
                    to="/instructor/kstack"
                    class="flex w-full flex-col items-center justify-center p-2 hover:bg-gray-300"
                    :class="{ 'bg-gray-300': isActive('/instructor/kstack') }"
                >
                    <img src="../../assets/images/stack.svg" alt="stack.svg" class="h-8" />
                    <span class="text-sm">Knowledge</span>
                    <span class="text-sm">Stack</span>
                </RouterLink>
            </div>
            <slot name="main-slot"></slot>
        </div>

        <!-- Todo: Create Separate Component for Drawer -->
        <!-- drawer toggle -->
        <button class="absolute bottom-6 right-6" @click="toggleDrawer">
            <img src="../../assets/images/ai.png" alt="ai.png" class="ai-btn h-12 cursor-pointer" />
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
                        <img src="../../assets/images/edit.svg" alt="cross.svg" class="h-6" />
                    </button>
                    <button class="rounded border border-black p-1 hover:bg-gray-100">
                        <img src="../../assets/images/bookmark.svg" alt="cross.svg" class="h-6" />
                    </button>
                    <button
                        class="rounded border border-black p-1 hover:bg-gray-100"
                        @click="toggleDrawer"
                    >
                        <img src="../../assets/images/cross.svg" alt="cross.svg" class="h-6" />
                    </button>
                </div>
            </div>

            <!-- body -->
            <div class="flex w-full h-full flex-1 overflow-y-scroll">
                <div class="flex flex-1 flex-col gap-2 items-center p-2 overflow-y-scroll">
                    <div class="ms-auto flex w-4/5 rounded-md bg-blue-200 p-2 mt-auto">
                        <p>What is 2 + 2 ?</p>
                    </div>
                    <div class="me-auto flex w-4/5 rounded-md bg-green-200 p-2">
                        <p>I can't give you the direct answer. But, you could get the answer by solving the expression 6 - 2 = ?.</p>
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
                        class="flex items-center justify-center rounded-md border p-1 px-2 hover:bg-gray-100"
                    >
                        <img src="../../assets/images/attach.svg" alt="cross.svg" class="h-6" />
                        <span class="text-sm">Context</span>
                    </button>
                    <button class="rounded-md border p-1.5 hover:bg-gray-100">
                        <img
                            src="../../assets/images/right-arrow.svg"
                            alt="cross.svg"
                            class="h-6"
                        />
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
