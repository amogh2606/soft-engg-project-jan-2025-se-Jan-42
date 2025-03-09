<script setup>
import { getAllChats } from '@/api';
import ChatbotDrawer from '@/components/ChatbotDrawer.vue';
import ExportIcon from '@/components/icons/ExportIcon.vue';
import EyeIcon from '@/components/icons/EyeIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import BaseView from '@/views/admin/BaseView.vue';
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
const filteredChats = computed(() =>
    chats.value.filter((chat) => chat.title.toLowerCase().includes(searchInput.value?.toLowerCase())),
);
const selectedChatId = ref(null);
const isDrawerOpen = ref(false);

const openChat = (chatId) => {
    selectedChatId.value = chatId;
    isDrawerOpen.value = true;
};

const closeDrawer = () => {
    isDrawerOpen.value = false;
    selectedChatId.value = null;
};

const syncChats = () => {
    getAllChats()
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
            syncChats();
        }
    },
    { immediate: true },
);

const downloadChats = () => {
    getAllChats(true)
        .then((response) => {
            // save as csv
            const blob = new Blob([response.data], { type: 'text/csv' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'chats.csv';
            a.click();
            push.success('Chats downloaded successfully !');
        })
        .catch((error) => {
            console.error(error);
            push.error('Error downloading chats !');
        });
};
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
                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                                v-model="searchInput"
                            />
                            <Button varient="primary">Search</Button>

                            <Button varient="primary" @click="downloadChats">
                                <ExportIcon :is-solid="false" class="h-6 w-auto" />
                            </Button>
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
