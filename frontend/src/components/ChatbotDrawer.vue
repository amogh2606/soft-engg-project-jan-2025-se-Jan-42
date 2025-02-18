<script setup>
import BookmarkIcon from '@/components/icons/BookmarkIcon.vue';
import CopyIcon from '@/components/icons/CopyIcon.vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';
import EditIcon from '@/components/icons/EditIcon.vue';
import SendIcon from '@/components/icons/SendIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import Dropdown from '@/components/ui/dropdown/Dropdown.vue';
import Modal from '@/components/ui/modal/Modal.vue';
import { useClipboard } from '@vueuse/core';
import { ref } from 'vue';

defineProps({
    closeDrawer: {
        type: Function,
        required: true,
    },
    isOpen: {
        type: Boolean,
        required: true,
    },
});

const contextList = ['Current Page', 'General FAQs', 'Coding', 'Lecture'];
const selectedContext = ref(null);
const isBookmarked = ref(false);
const toggleBookmark = () => {
    isBookmarked.value = !isBookmarked.value;
};

const chatTitle = ref('Chat Title Here ...');
const _chatTitle = ref(chatTitle.value);
const isEditModalOpen = ref(false);
const updateChatTitle = () => {
    chatTitle.value = _chatTitle.value;
    isEditModalOpen.value = false;
};
const toggleEditModal = () => {
    isEditModalOpen.value = !isEditModalOpen.value;
    _chatTitle.value = chatTitle.value;
};

const { copy } = useClipboard();
</script>
<template>
    <!-- drawer component -->
    <Transition name="fade">
        <div
            v-if="isOpen"
            class="absolute right-0 top-0 h-screen w-screen bg-black opacity-50"
            id="overlay"
        ></div>
    </Transition>
    <Transition name="slide">
        <div
            v-if="isOpen"
            class="absolute right-0 top-0 flex h-screen w-full flex-col bg-white sm:w-1/2 md:w-1/3"
            id="drawer"
        >
            <!-- header -->
            <div class="flex items-center justify-between border-b bg-gray-50 p-2">
                <p class="text-lg">{{ chatTitle }}</p>
                <div class="flex gap-2">
                    <Button varient="light" class="rounded-full !p-1.5" @click="toggleEditModal">
                        <EditIcon class="h-6 w-auto" />
                    </Button>
                    <Button varient="light" class="rounded-full !p-1.5" @click="toggleBookmark">
                        <BookmarkIcon :is-solid="isBookmarked" class="h-6 w-auto" />
                    </Button>
                    <Button varient="light" class="rounded-full !p-1.5" @click="closeDrawer">
                        <CrossIcon class="h-6 w-auto" />
                    </Button>
                </div>
            </div>

            <!-- body -->
            <div class="flex h-full w-full flex-1 overflow-y-scroll">
                <div class="flex flex-1 flex-col items-center gap-2 overflow-y-scroll p-2">
                    <div class="ms-auto mt-auto flex w-4/5 rounded-md bg-blue-200 p-2">
                        <p>What is 2 + 2 ?</p>
                        <button
                            class="ms-auto mt-auto opacity-50 transition-opacity hover:opacity-100"
                            @click="copy('copy message')"
                        >
                            <CopyIcon class="h-4 w-4" />
                        </button>
                    </div>
                    <div class="me-auto flex w-4/5 rounded-md bg-green-200 p-2">
                        <p>
                            I can't give you the direct answer. But, you could get the answer by
                            solving the expression 6 - 2 = ?.
                        </p>
                        <button
                            class="ms-auto mt-auto opacity-50 transition-opacity hover:opacity-100"
                            @click="copy('copy message')"
                        >
                            <CopyIcon class="h-4 w-4" />
                        </button>
                    </div>
                    <div class="ms-auto flex w-4/5 rounded-md bg-blue-200 p-2">
                        <p>Got it ! Thanks :)</p>
                        <button
                            class="ms-auto mt-auto opacity-50 transition-opacity hover:opacity-100"
                            @click="copy('copy message')"
                        >
                            <CopyIcon class="h-4 w-4" />
                        </button>
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
    </Transition>

    <!-- edit modal -->
    <Modal v-model="isEditModalOpen" :show-close-button="false">
        <div class="flex flex-col gap-2">
            <input type="text" v-model="_chatTitle" class="w-full rounded-md border p-2" />
            <div class="flex items-center justify-end gap-2">
                <Button varient="secondary" @click="toggleEditModal"> Cancel </Button>
                <Button varient="primary" @click="updateChatTitle"> Save </Button>
            </div>
        </div>
    </Modal>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
    transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
    transform: translateX(100%);
}
</style>
