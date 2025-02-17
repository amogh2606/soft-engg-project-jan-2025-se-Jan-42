<script setup>
import BookmarkIcon from '@/components/icons/BookmarkIcon.vue';
import ChatbotIcon from '@/components/icons/ChatbotIcon.vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';
import EditIcon from '@/components/icons/EditIcon.vue';
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import ModulesIcon from '@/components/icons/ModulesIcon.vue';
import SendIcon from '@/components/icons/SendIcon.vue';
import UserIcon from '@/components/icons/UserIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import Dropdown from '@/components/ui/dropdown/Dropdown.vue';
import Modal from '@/components/ui/modal/Modal.vue';
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const drawerOpen = ref(false);
const toggleDrawer = () => {
    drawerOpen.value = !drawerOpen.value;
};
const showWeeklyIndex = ref(true);
const contextList = ['Current Page', 'General FAQs', 'Coding', 'Lecture'];
const selectedContext = ref(null);
const isBookmarked = ref(false);
const toggleBookmark = () => {
    isBookmarked.value = !isBookmarked.value;
};

const chatTitle = ref('Chat Title Here ...');
const _chatTitle = ref(chatTitle.value);
const isModalOpen = ref(false);
const updateChatTitle = () => {
    chatTitle.value = _chatTitle.value;
    isModalOpen.value = false;
};
const toggleModal = () => {
    isModalOpen.value = !isModalOpen.value;
    _chatTitle.value = chatTitle.value;
};
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
            <div class="flex items-center justify-between border-b bg-gray-50 p-2">
                <p class="text-lg">{{ chatTitle }}</p>
                <div class="flex gap-2">
                    <Button varient="light" class="rounded-full !p-1.5" @click="toggleModal">
                        <EditIcon class="h-6 w-auto" />
                    </Button>
                    <Button varient="light" class="rounded-full !p-1.5" @click="toggleBookmark">
                        <BookmarkIcon :is-solid="isBookmarked" class="h-6 w-auto" />
                    </Button>

                    <Button varient="light" class="rounded-full !p-1.5" @click="toggleDrawer">
                        <CrossIcon class="h-6 w-auto" />
                    </Button>
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
            <div class="m-2 flex flex-col rounded-md border border-gray-400">
                <textarea
                    type="text"
                    class="w-full resize-none rounded p-2 outline-none"
                    placeholder="Type a message ..."
                ></textarea>
                <div class="flex items-center justify-between p-2">
                    <Dropdown :options="contextList" v-model="selectedContext" />
                    <button class="rounded-md border p-1.5 hover:bg-gray-100">
                        <SendIcon :is-solid="true" class="h-6 w-6" />
                    </button>
                </div>
            </div>
        </div>
        <Modal v-model="isModalOpen" :show-close-button="false">
            <div class="flex flex-col gap-2">
                <input type="text" v-model="_chatTitle" class="w-full rounded-md border p-2" />
                <div class="flex items-center justify-end gap-2">
                    <Button varient="secondary" @click="toggleModal"> Cancel </Button>
                    <Button varient="primary" @click="updateChatTitle"> Save </Button>
                </div>
            </div>
        </Modal>
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
