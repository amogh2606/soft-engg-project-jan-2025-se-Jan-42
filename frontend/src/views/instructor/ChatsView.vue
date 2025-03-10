<script setup>
import { getUserChats } from '@/api';
import ChatbotDrawer from '@/components/ChatbotDrawer.vue';
import EyeIcon from '@/components/icons/EyeIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import BaseView from '@/views/instructor/BaseView.vue';
import { push } from 'notivue';
import { computed, ref, watch } from 'vue';

const headers = [
    { key: 'id', label: 'Id' },
    { key: 'title', label: 'Title' },
    { key: 'created', label: 'Created At' },
    { key: 'actions', label: 'Actions' },
];
const searchInput = ref('');
const chats = ref([]);
const filterBookmarked = ref(false);
const selectedChatId = ref(null);
const isDrawerOpen = ref(false);

const filteredChats = computed(() => {
    const filteredChats = chats.value.filter((chat) =>
        chat.title.toLowerCase().includes(searchInput.value?.toLowerCase()),
    );
    return filterBookmarked.value ? filteredChats.filter((chat) => chat.bookmarked) : filteredChats;
});

const openChat = (chatId) => {
    selectedChatId.value = chatId;
    isDrawerOpen.value = true;
};

const closeDrawer = () => {
    isDrawerOpen.value = false;
    selectedChatId.value = null;
};

const syncUserChats = () => {
    getUserChats()
        .then((response) => {
            chats.value = response.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching chats !');
        });
};

watch(
    isDrawerOpen,
    (newVal) => {
        if (!newVal) {
            syncUserChats();
        }
    },
    { immediate: true },
);
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">
                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded-lg border bg-white p-4 shadow md:mx-10 md:mb-10"
                >
                    <h1 class="p-3 pb-7 text-center text-2xl font-semibold md:mx-10 md:px-8">
                        ChatBot Conversations
                    </h1>
                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex flex-wrap justify-between gap-2 border-b p-3">
                            <div class="flex items-center gap-2">
                                <input
                                    type="text"
                                    class="w-full rounded border p-2"
                                    placeholder="Search..."
                                    v-model="searchInput"
                                />
                                <Button varient="primary">Search</Button>
                            </div>
                            <label for="toggle" class="flex cursor-pointer items-center space-x-3">
                                <div class="relative">
                                    <input
                                        type="checkbox"
                                        id="toggle"
                                        class="peer sr-only"
                                        v-model="filterBookmarked"
                                    />
                                    <div
                                        class="block h-6 w-12 rounded-full bg-gray-300 transition-all peer-checked:bg-blue-500"
                                    ></div>
                                    <div
                                        class="absolute left-1 top-1 h-4 w-4 rounded-full bg-white transition-all peer-checked:left-7"
                                    ></div>
                                </div>
                                <span class="text-gray-700">Bookmark Only</span>
                            </label>
                        </div>
                        <TableComponent :headers="headers" :rows="filteredChats">
                            <template #actions="{ row }">
                                <Button varient="light" :rounded="true" @click="openChat(row.id)">
                                    <EyeIcon :is-solid="false" class="h-6 w-6" />
                                </Button>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
    <ChatbotDrawer
        :is-open="isDrawerOpen"
        :close-drawer="closeDrawer"
        :read-only="true"
        :chat-id="selectedChatId"
    />
</template>
