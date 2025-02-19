<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';

const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'Feedback', key: 'feedback' },
    { label: 'Created At', key: 'createdAt' },
]);
const feedbacks = ref([
    {
        id: 1,
        feedback: 'Software Eng...',
        createdAt: '2021-09-01 12:00:00',
    },
    {
        id: 2,
        feedback: 'Data Struct...',
        createdAt: '2021-09-02 12:00:00',
    },
    {
        id: 3,
        feedback: 'Operating Systems',
        createdAt: '2021-09-03 12:00:00',
    },
    {
        id: 4,
        feedback: 'Computer Networks',
        createdAt: '2021-09-04 12:00:00',
    },
    {
        id: 5,
        feedback: 'Database Mana...',
        createdAt: '2021-09-05 12:00:00',
    },
    {
        id: 6,
        feedback: 'Computer Archi...',
        createdAt: '2021-09-06 12:00:00',
    },
    {
        id: 7,
        feedback: 'Artificial Int...',
        createdAt: '2021-09-07 12:00:00',
    },
    {
        id: 8,
        feedback: 'Machine Learn...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 9,
        feedback: 'Machine Learn...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 10,
        feedback: 'Natural Langu...',
        createdAt: '2021-09-10 12:00:00',
    },
    {
        id: 11,
        feedback: 'Software Eng...',
        createdAt: '2021-09-11 12:00:00',
    },
    {
        id: 12,
        feedback: 'Data Struct...',
        createdAt: '2021-09-12 12:00:00',
    },
    {
        id: 13,
        feedback: 'Operating Systems',
        createdAt: '2021-09-13 12:00:00',
    },
    {
        id: 14,
        feedback: 'Computer Networks',
        createdAt: '2021-09-14 12:00:00',
    },
    {
        id: 15,
        feedback: 'Database Mana...',
        createdAt: '2021-09-15 12:00:00',
    },
    {
        id: 16,
        feedback: 'Computer Archi...',
        createdAt: '2021-09-16 12:00:00',
    },
    {
        id: 17,
        feedback: 'Artificial Int...',
        createdAt: '2021-09-17 12:00:00',
    },
    {
        id: 18,
        feedback: 'Machine Learn...',
        createdAt: '2021-09-18 12:00:00',
    },
    {
        id: 19,
        feedback: 'Deep Learning',
        createdAt: '2021-09-19 12:00:00',
    },
    {
        id: 20,
        feedback: 'Natural Langu...',
        createdAt: '2021-09-20 12:00:00',
    },
]);
const filteredFeedbacks = computed(() => {
    return feedbacks.value;
});
</script>
<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">
                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded-lg border bg-white p-4 shadow md:mx-10 md:mb-10"
                >
                    <h1 class="p-3 pb-7 text-center text-2xl font-semibold md:mx-10 md:px-8">
                        Student Feedbacks
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                            />
                            <Button varient="primary">Search</Button>
                        </div>
                        <TableComponent :headers="headers" :data="filteredFeedbacks" />
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
