<script setup>
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';
import Button from '@/components/ui/buttons/Button.vue';

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
                <h1 class="p-3 text-center text-2xl font-semibold md:mx-10 md:px-8">
                    Feedbacks
                </h1>

                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded border bg-gray-50 shadow md:mx-10 md:mb-10"
                >
                    <!-- search box -->
                    <div class="flex justify-between gap-2 p-3">
                        <input
                            type="text"
                            class="w-full rounded border p-2"
                            placeholder="Search..."
                        />
                        <Button varient="primary">Search</Button>
                    </div>

                    <!-- Wrap the table in a scrollable container -->
                    <div class="overflow-y-auto">
                        <table class="w-full divide-y">
                            <thead class="sticky top-0 bg-yellow-50 shadow">
                                <tr class="divide-x">
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                    >
                                        Id
                                    </th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                    >
                                        Feedback
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
                                    v-for="feedback in filteredFeedbacks"
                                    :key="feedback.id"
                                    class="divide-x even:bg-gray-50"
                                >
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ feedback.id }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ feedback.feedback }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ feedback.createdAt }}</div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
