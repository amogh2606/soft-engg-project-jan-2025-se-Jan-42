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
import { push } from 'notivue';
import { nextTick, ref, watch } from 'vue';

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

const chats = ref([
    {
        id: 1,
        message: 'What is 2 + 2 ?',
        user: 'user',
    },
    {
        id: 2,
        message:
            "I can't give you the direct answer. But, you could get the answer by solving the expression 6 - 2 = ?.",
        user: 'assistant',
    },
    {
        id: 3,
        message: 'Got it ! Thanks :)',
        user: 'user',
    },
]);

const contextList = ['Current Page', 'General FAQs', 'Coding', 'Lecture'];
const selectedContext = ref(null);
const isBookmarked = ref(false);
const toggleBookmark = () => {
    isBookmarked.value = !isBookmarked.value;
    push.success({
        message: isBookmarked.value ? 'Bookmark added' : 'Bookmark removed',
    });
};

const chatTitle = ref('Chat Title Here ...');
const _chatTitle = ref(chatTitle.value);
const isEditModalOpen = ref(false);
const updateChatTitle = () => {
    chatTitle.value = _chatTitle.value;
    isEditModalOpen.value = false;
    push.success({
        message: 'Chat title updated',
    });
};
const toggleEditModal = () => {
    isEditModalOpen.value = !isEditModalOpen.value;
    _chatTitle.value = chatTitle.value;
};

const { copy } = useClipboard();
const copyMessage = (message) => {
    copy(message);
    push.success({
        message: 'Message copied',
    });
};

const newMessage = ref('');
const chatContainer = ref(null);

const scrollToBottom = () => {
    if (chatContainer.value) {
        chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
    }
};

watch(
    chats,
    () => {
        // Use nextTick to ensure DOM is updated before scrolling
        nextTick(() => {
            scrollToBottom();
        });
    },
    { deep: true },
);

const sendMessage = () => {
    if (newMessage.value.trim() === '') return;
    chats.value.push({
        id: chats.value.length + 1,
        message: newMessage.value,
        user: 'user',
    });
    newMessage.value = '';
    setTimeout(() => {
        chats.value.push({
            id: chats.value.length + 1,
            message: 'Thanks for your message !',
            user: 'assistant',
        });
    }, 1000);
};
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
                    <Button varient="light" :rounded="true" @click="toggleEditModal">
                        <EditIcon class="h-6 w-auto" />
                    </Button>
                    <Button varient="light" :rounded="true" @click="toggleBookmark">
                        <BookmarkIcon :is-solid="isBookmarked" class="h-6 w-auto" />
                    </Button>
                    <Button varient="light" :rounded="true" @click="closeDrawer">
                        <CrossIcon class="h-6 w-auto" />
                    </Button>
                </div>
            </div>

            <!-- body -->
            <div ref="chatContainer" class="flex h-full w-full flex-1 overflow-y-scroll">
                <div
                    class="flex flex-1 flex-col items-center gap-2 overflow-y-scroll p-2 first:mt-auto"
                >
                    <div
                        v-for="chat in chats"
                        :key="chat.id"
                        class="flex w-4/5 rounded-md p-2"
                        :class="{
                            'bg-green-200': chat.user === 'assistant',
                            'bg-blue-200': chat.user === 'user',
                            'ms-auto': chat.user === 'user',
                            'me-auto': chat.user === 'assistant',
                        }"
                    >
                        <p>{{ chat.message }}</p>
                        <button
                            class="ms-auto mt-auto opacity-50 transition-opacity hover:opacity-100"
                            @click="copyMessage(chat.message)"
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
                    v-model="newMessage"
                    @keydown.enter.prevent="sendMessage"
                ></textarea>
                <div class="flex items-center justify-between p-2">
                    <Dropdown :options="contextList" v-model="selectedContext" />
                    <button class="rounded-md border p-1.5 hover:bg-gray-100" @click="sendMessage">
                        <SendIcon :is-solid="true" class="h-6 w-6" />
                    </button>
                </div>
            </div>
        </div>
    </Transition>

    <!-- edit modal -->
    <Modal v-model="isEditModalOpen" :show-close-button="false">
        <div class="flex flex-col gap-2">
            <p class="text-lg font-semibold tracking-wide">Edit Chat Title</p>
            <input
                type="text"
                v-model="_chatTitle"
                class="text-md w-full rounded-md border border-gray-300 px-4 py-2 text-gray-700 shadow-sm focus:outline-none focus:ring-1 focus:ring-gray-400"
            />
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

.slide-enter-active {
    transition: transform 0.3s ease;
}

.slide-enter-from {
    transform: translateX(100%);
}

.slide-leave-active {
    transition: opacity 0.3s ease;
}

.slide-leave-to {
    opacity: 0;
}
</style>
