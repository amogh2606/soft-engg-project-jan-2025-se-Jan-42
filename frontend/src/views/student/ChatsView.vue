<script setup>
import BaseView from './BaseView.vue';
import { ref, computed } from 'vue';

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
        <template #right-slot>
            <div class="flex flex-1 flex-col pt-4">
                <h1 class="p-3 text-center text-2xl font-semibold md:mx-10 md:px-8">
                    ChatBot Conversations
                </h1>
                <div
                    class="mx-2 mb-2 flex flex-col overflow-y-hidden rounded border bg-gray-50 shadow md:mx-10 md:mb-10"
                >
                    <div class="flex items-center border-b bg-gray-400 p-3 px-3 md:px-8">
                        <label class="relative ms-auto inline-flex cursor-pointer items-center">
                            <input
                                type="checkbox"
                                class="peer sr-only"
                                name="bookmark-only"
                                id="bookmark-only"
                                v-model="bookmarkOnly"
                            />
                            <div
                                class="peer h-6 w-11 rounded-full bg-gray-200 peer-checked:bg-black after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5 after:rounded-full after:border after:border-gray-300 after:bg-white after:transition-all after:content-[''] peer-checked:after:translate-x-full peer-checked:after:border-white"
                            ></div>
                            <span class="ml-3">Bookmarked Only</span>
                        </label>
                    </div>
                    <div v-if="filteredChats.length === 0" class="p-3 text-center">
                        No chats available !
                    </div>
                    <div
                        v-else
                        class="flex flex-col gap-2 overflow-y-scroll scroll-smooth p-3 !pt-2 md:p-8"
                    >
                        <div
                            v-for="chat in filteredChats"
                            :key="chat.id"
                            class="grid cursor-pointer columns-2 grid-cols-3 rounded border border-gray-300 bg-white shadow hover:bg-gray-100"
                        >
                            <p class="p-2">{{ chat.title }}</p>
                            <span class="ms-auto h-full w-[2px] bg-gray-300"></span>
                            <p class="p-2">{{ chat.createdAt }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
