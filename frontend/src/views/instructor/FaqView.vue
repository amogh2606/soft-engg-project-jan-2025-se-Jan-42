<script setup>
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';

const chats = ref([
    {
        id: 1,
        question: 'Software Eng...',
        createdAt: '2021-09-01 12:00:00',
        category: 'category...',
    },
    {
        id: 2,
        question: 'Data Struct...',
        createdAt: '2021-09-02 12:00:00',
        category: 'category...',
    },
    {
        id: 3,
        question: 'Operating Systems',
        createdAt: '2021-09-03 12:00:00',
        category: 'category...',
    },
    {
        id: 4,
        question: 'Computer Networks',
        createdAt: '2021-09-04 12:00:00',
        category: 'category...',
    },
    {
        id: 5,
        question: 'Database Mana...',
        createdAt: '2021-09-05 12:00:00',
        category: 'category...',
    },
    {
        id: 6,
        question: 'Computer Archi...',
        createdAt: '2021-09-06 12:00:00',
        category: 'category...',
    },
    {
        id: 7,
        question: 'Artificial Int...',
        createdAt: '2021-09-07 12:00:00',
        category: 'category...',
    },
    {
        id: 8,
        question: 'Machine Learn...',
        createdAt: '2021-09-08 12:00:00',
        category: 'category...',
    },
    { id: 9, question: 'Deep Learning', createdAt: '2021-09-09 12:00:00', category: 'category...' },
    {
        id: 10,
        question: 'Natural Langu...',
        createdAt: '2021-09-10 12:00:00',
        category: 'category...',
    },
    {
        id: 11,
        question: 'Software Eng...',
        createdAt: '2021-09-11 12:00:00',
        category: 'category...',
    },
    {
        id: 12,
        question: 'Data Struct...',
        createdAt: '2021-09-12 12:00:00',
        category: 'category...',
    },
    {
        id: 13,
        question: 'Operating Systems',
        createdAt: '2021-09-13 12:00:00',
        category: 'category...',
    },
    {
        id: 14,
        question: 'Computer Networks',
        createdAt: '2021-09-14 12:00:00',
        category: 'category...',
    },
    {
        id: 15,
        question: 'Database Mana...',
        createdAt: '2021-09-15 12:00:00',
        category: 'category...',
    },
    {
        id: 16,
        question: 'Computer Archi...',
        createdAt: '2021-09-16 12:00:00',
        category: 'category...',
    },
    {
        id: 17,
        question: 'Artificial Int...',
        createdAt: '2021-09-17 12:00:00',
        category: 'category...',
    },
    {
        id: 18,
        question: 'Machine Learn...',
        createdAt: '2021-09-18 12:00:00',
        category: 'category...',
    },
    {
        id: 19,
        question: 'Deep Learning',
        createdAt: '2021-09-19 12:00:00',
        category: 'category...',
    },
    {
        id: 20,
        question: 'Natural Langu...',
        createdAt: '2021-09-20 12:00:00',
        category: 'category...',
    },
]);
const filteredChats = computed(() => {
    return chats.value;
});
</script>
<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col pt-4">
                <h1 class="p-3 text-center text-2xl font-semibold md:mx-10 md:px-8">
                    Frequently Asked Questions
                </h1>
                <div
                    class="mx-2 mb-2 flex flex-col overflow-y-hidden rounded border bg-gray-50 shadow md:mx-10 md:mb-10"
                >
                    <div v-if="filteredChats.length === 0" class="p-3 text-center">
                        No chats available !
                    </div>


                </div>
            </div>
        </template>
    </BaseView>
</template>
