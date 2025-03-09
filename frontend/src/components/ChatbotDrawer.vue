<script setup>
import { getChatbotSession, sendMessageToChatbot, updateChatbotSession } from '@/api';
import BookmarkIcon from '@/components/icons/BookmarkIcon.vue';
import CopyIcon from '@/components/icons/CopyIcon.vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';
import EditIcon from '@/components/icons/EditIcon.vue';
import ResetIcon from '@/components/icons/ResetIcon.vue';
import SendIcon from '@/components/icons/SendIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import Dropdown from '@/components/ui/dropdown/ContextDropdown.vue';
import Modal from '@/components/ui/modal/Modal.vue';
import { useAuthStore } from '@/stores/auth';
import { useClipboard } from '@vueuse/core';
import { push } from 'notivue';
import { ref, watchEffect } from 'vue';

const props = defineProps({
    closeDrawer: {
        type: Function,
        required: true,
    },
    isOpen: {
        type: Boolean,
        required: true,
    },
});

const { user } = useAuthStore();
const { copy } = useClipboard();

const session = ref(null);
const chatTitleInput = ref('Chat Title Here ...');
const isEditTitleModalOpen = ref(false);
const newMessage = ref('');
const chatContainer = ref(null);
const selectedCourse = ref(null);
const courseList = user.courses.map((course) => course.name);

const refreshSession = () => {
    getChatbotSession()
        .then((res) => {
            session.value = res.data;
            selectedCourse.value = null;
            newMessage.value = '';
            setTimeout(() => scrollToBottom(), 500);
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching session !');
        });
};

const toggleBookmark = () => {
    updateChatbotSession(session.value.id, session.value.title, !session.value.bookmarked)
        .then((res) => {
            session.value = res.data;
            push.success({
                message: session.value.bookmarked ? 'Bookmark added' : 'Bookmark removed',
            });
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong updating session !');
        });
};

const updateChatTitle = () => {
    updateChatbotSession(session.value.id, chatTitleInput.value, session.value.bookmarked)
        .then((res) => {
            session.value = res.data;
            push.success({
                message: 'Chat title updated',
            });
            toggleEditTitleModal();
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong updating session !');
        });
};

const toggleEditTitleModal = () => {
    isEditTitleModalOpen.value = !isEditTitleModalOpen.value;
    chatTitleInput.value = session.value.title;
};

const sendMessage = () => {
    if (newMessage.value.trim() === '') return;
    const courseId = user.courses.find((course) => course.name === selectedCourse.value)?.id;

    sendMessageToChatbot(session.value.id, newMessage.value, courseId)
        .then((res) => {
            refreshSession();
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong sending message !');
        });
};

const copyMessage = (message) => {
    copy(message);
    push.success({
        message: 'Message copied',
    });
};

const scrollToBottom = () => {
    if (chatContainer.value) {
        chatContainer.value.scrollTo({
            top: chatContainer.value.scrollHeight,
            behavior: 'smooth',
        });
    }
};

watchEffect(() => {
    if (props.isOpen) {
        refreshSession();
    }
});
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
                <p class="text-lg">{{ session?.title }}</p>
                <div class="flex gap-2">
                    <Button varient="light" :rounded="true" @click="toggleEditTitleModal">
                        <EditIcon class="h-5 w-auto" />
                    </Button>
                    <Button varient="light" :rounded="true" @click="toggleBookmark">
                        <BookmarkIcon :is-solid="session?.bookmarked" class="h-5 w-auto" />
                    </Button>
                    <Button varient="light" :rounded="true" @click="closeDrawer">
                        <CrossIcon class="h-5 w-auto" />
                    </Button>
                </div>
            </div>

            <!-- body -->
            <div ref="chatContainer" class="flex h-full w-full flex-1 overflow-y-scroll">
                <div
                    class="flex flex-1 flex-col items-center gap-2 overflow-y-scroll p-2 first:mt-auto"
                >
                    <div
                        v-for="msg in session?.messages"
                        :key="msg.id"
                        class="flex w-4/5 rounded-lg px-3 py-2"
                        :class="{
                            'bg-gray-100': msg?.is_response,
                            'bg-blue-100': !msg?.is_response,
                            'me-auto': msg?.is_response,
                            'ms-auto': !msg?.is_response,
                            'rounded-tl-none': msg?.is_response,
                            'rounded-tr-none': !msg?.is_response,
                        }"
                    >
                        <p class="whitespace-pre-line">{{ msg.text }}</p>
                        <button
                            class="ms-auto mt-auto opacity-50 transition-opacity hover:opacity-100"
                            @click="copyMessage(msg.text)"
                        >
                            <CopyIcon class="h-3.5 w-auto" />
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
                    @keydown.enter.exact.prevent="sendMessage"
                    @keydown.shift.enter.prevent="newMessage += '\n'"
                ></textarea>
                <div class="flex items-center justify-between p-2">
                    <div class="flex items-center gap-2">
                        <Dropdown :options="courseList" v-model="selectedCourse" />
                        <Button
                            v-if="selectedCourse !== null"
                            varient="light"
                            :rounded="true"
                            @click="selectedCourse = null"
                        >
                            <ResetIcon class="h-3 w-auto" />
                        </Button>
                    </div>
                    <Button
                        varient="secondary"
                        :rounded="true"
                        :disabled="newMessage.trim() === ''"
                        @click="sendMessage"
                    >
                        <SendIcon :is-solid="true" class="h-5 w-auto" />
                    </Button>
                </div>
            </div>
        </div>
    </Transition>

    <!-- edit modal -->
    <Modal v-model="isEditTitleModalOpen" :show-close-button="false">
        <div class="flex flex-col gap-2">
            <p class="text-lg font-semibold tracking-wide">Edit Chat Title</p>
            <input
                type="text"
                v-model="chatTitleInput"
                class="text-md w-full rounded-md border border-gray-300 px-4 py-2 text-gray-700 shadow-sm focus:outline-none focus:ring-1 focus:ring-gray-400"
            />
            <div class="flex items-center justify-end gap-2">
                <Button varient="secondary" @click="toggleEditTitleModal"> Cancel </Button>
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
