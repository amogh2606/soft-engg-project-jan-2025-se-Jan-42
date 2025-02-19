<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import BaseView from '@/views/student/BaseView.vue';
import { computed, ref } from 'vue';

const headers = [
    { key: 'id', label: 'Id' },
    { key: 'title', label: 'Title' },
    { key: 'createdAt', label: 'Created At' },
];
const chats = ref([
    { id: 1, title: 'Software Eng...', createdAt: '2021-09-01 12:00:00', isBookmarked: true },
    { id: 2, title: 'Data Struct...', createdAt: '2021-09-02 12:00:00', isBookmarked: false },
    { id: 3, title: 'Operating Systems', createdAt: '2021-09-03 12:00:00', isBookmarked: true },
    { id: 4, title: 'Software Eng...', createdAt: '2021-09-01 12:00:00', isBookmarked: true },
    { id: 5, title: 'Data Struct...', createdAt: '2021-09-02 12:00:00', isBookmarked: false },
    { id: 6, title: 'Operating Systems', createdAt: '2021-09-03 12:00:00', isBookmarked: true },
    { id: 7, title: 'Software Eng...', createdAt: '2021-09-01 12:00:00', isBookmarked: true },
    { id: 8, title: 'Data Struct...', createdAt: '2021-09-02 12:00:00', isBookmarked: false },
    { id: 9, title: 'Operating Systems', createdAt: '2021-09-03 12:00:00', isBookmarked: true },
    { id: 10, title: 'Software Eng...', createdAt: '2021-09-01 12:00:00', isBookmarked: true },
    { id: 11, title: 'Data Struct...', createdAt: '2021-09-02 12:00:00', isBookmarked: false },
    { id: 12, title: 'Operating Systems', createdAt: '2021-09-03 12:00:00', isBookmarked: true },
]);

const bookmarkOnly = ref(false);
const filteredChats = computed(() =>
    bookmarkOnly.value ? chats.value.filter((chat) => chat.isBookmarked) : chats.value,
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
                                />
                                <Button varient="primary">Search</Button>
                            </div>
                            <label for="toggle" class="flex cursor-pointer items-center space-x-3">
                                <div class="relative">
                                    <input
                                        type="checkbox"
                                        id="toggle"
                                        class="peer sr-only"
                                        v-model="bookmarkOnly"
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
                        <TableComponent :headers="headers" :data="filteredChats" />
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
