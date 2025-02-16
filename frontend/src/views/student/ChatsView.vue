<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';

const chats = ref([
    { id: 1, title: 'Software Eng...', createdAt: '2021-09-01 12:00:00', isBookmarked: true },
    { id: 2, title: 'Data Struct...', createdAt: '2021-09-02 12:00:00', isBookmarked: false },
    { id: 3, title: 'Operating Systems', createdAt: '2021-09-03 12:00:00', isBookmarked: true },
    { id: 4, title: 'Computer Networks', createdAt: '2021-09-04 12:00:00', isBookmarked: false },
    { id: 5, title: 'Database Mana...', createdAt: '2021-09-05 12:00:00', isBookmarked: true },
    { id: 6, title: 'Computer Archi...', createdAt: '2021-09-06 12:00:00', isBookmarked: false },
    { id: 7, title: 'Artificial Int...', createdAt: '2021-09-07 12:00:00', isBookmarked: true },
    { id: 8, title: 'Machine Learn...', createdAt: '2021-09-08 12:00:00', isBookmarked: false },
    { id: 9, title: 'Deep Learning', createdAt: '2021-09-09 12:00:00', isBookmarked: true },
    { id: 10, title: 'Natural Langu...', createdAt: '2021-09-10 12:00:00', isBookmarked: false },
    { id: 11, title: 'Software Eng...', createdAt: '2021-09-11 12:00:00', isBookmarked: true },
    { id: 12, title: 'Data Struct...', createdAt: '2021-09-12 12:00:00', isBookmarked: false },
    { id: 13, title: 'Operating Systems', createdAt: '2021-09-13 12:00:00', isBookmarked: true },
    { id: 14, title: 'Computer Networks', createdAt: '2021-09-14 12:00:00', isBookmarked: false },
    { id: 15, title: 'Database Mana...', createdAt: '2021-09-15 12:00:00', isBookmarked: true },
    { id: 16, title: 'Computer Archi...', createdAt: '2021-09-16 12:00:00', isBookmarked: false },
    { id: 17, title: 'Artificial Int...', createdAt: '2021-09-17 12:00:00', isBookmarked: true },
    { id: 18, title: 'Machine Learn...', createdAt: '2021-09-18 12:00:00', isBookmarked: false },
    { id: 19, title: 'Deep Learning', createdAt: '2021-09-19 12:00:00', isBookmarked: true },
    { id: 20, title: 'Natural Langu...', createdAt: '2021-09-20 12:00:00', isBookmarked: false },
]);

const bookmarkOnly = ref(false);
const filteredChats = computed(() => {
    return bookmarkOnly.value ? chats.value.filter((chat) => chat.isBookmarked) : chats.value;
});
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">

                <div class="flex flex-col mx-2 mb-2 rounded-lg border bg-white p-4 overflow-hidden  shadow md:mx-10 md:mb-10">
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
                                        class="block h-6 w-12 rounded-full bg-gray-300 transition-all peer-checked:bg-black"
                                    ></div>
                                    <div
                                        class="absolute left-1 top-1 h-4 w-4 rounded-full bg-white transition-all peer-checked:left-7"
                                    ></div>
                                </div>
                                <span class="text-gray-700">Bookmark Only</span>
                            </label>
                        </div>

                        <!-- Wrap the table in a scrollable container -->
                        <div class="overflow-y-auto">
                            <table class="w-full divide-y">
                                <thead class="sticky top-0 bg-gray-300 shadow">
                                    <tr class="divide-x">
                                        <th
                                            class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                        >
                                            Id
                                        </th>
                                        <th
                                            class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                        >
                                            Title
                                        </th>
                                        <th
                                            class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                        >
                                            Created At
                                        </th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y bg-white">
                                    <tr
                                        v-for="chat in filteredChats"
                                        :key="chat.id"
                                        class="cursor-pointer divide-x hover:bg-gray-50"
                                    >
                                        <td class="whitespace-nowrap px-6 py-4">
                                            <div class="text-sm text-gray-900">{{ chat.id }}</div>
                                        </td>
                                        <td class="whitespace-nowrap px-6 py-4">
                                            <div class="text-sm text-gray-900">
                                                {{ chat.title }}
                                            </div>
                                        </td>
                                        <td class="whitespace-nowrap px-6 py-4">
                                            <div class="text-sm text-gray-900">
                                                {{ chat.createdAt }}
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
