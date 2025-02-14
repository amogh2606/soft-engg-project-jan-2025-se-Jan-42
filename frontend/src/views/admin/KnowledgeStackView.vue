<script setup>
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';

const files = ref([
    {
        id: 1,
        fileName: 'Software Eng...',
        createdAt: '2021-09-01 12:00:00',
    },
    {
        id: 2,
        fileName: 'Data Struct...',
        createdAt: '2021-09-02 12:00:00',
    },
    {
        id: 3,
        fileName: 'Operating Systems',
        createdAt: '2021-09-03 12:00:00',
    },
    {
        id: 4,
        fileName: 'Computer Networks',
        createdAt: '2021-09-04 12:00:00',
    },
    {
        id: 5,
        fileName: 'Database Mana...',
        createdAt: '2021-09-05 12:00:00',
    },
    {
        id: 6,
        fileName: 'Computer Archi...',
        createdAt: '2021-09-06 12:00:00',
    },
    {
        id: 7,
        fileName: 'Artificial Int...',
        createdAt: '2021-09-07 12:00:00',
    },
    {
        id: 8,
        fileName: 'Machine Learn...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 9,
        fileName: 'Machine Learn...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 10,
        fileName: 'Natural Langu...',
        createdAt: '2021-09-10 12:00:00',
    },
    {
        id: 11,
        fileName: 'Software Eng...',
        createdAt: '2021-09-11 12:00:00',
    },
    {
        id: 12,
        fileName: 'Data Struct...',
        createdAt: '2021-09-12 12:00:00',
    },
    {
        id: 13,
        fileName: 'Operating Systems',
        createdAt: '2021-09-13 12:00:00',
    },
    {
        id: 14,
        fileName: 'Computer Networks',
        createdAt: '2021-09-14 12:00:00',
    },
    {
        id: 15,
        fileName: 'Database Mana...',
        createdAt: '2021-09-15 12:00:00',
    },
    {
        id: 16,
        fileName: 'Computer Archi...',
        createdAt: '2021-09-16 12:00:00',
    },
    {
        id: 17,
        fileName: 'Artificial Int...',
        createdAt: '2021-09-17 12:00:00',
    },
    {
        id: 18,
        fileName: 'Machine Learn...',
        createdAt: '2021-09-18 12:00:00',
    },
    {
        id: 19,
        fileName: 'Deep Learning',
        createdAt: '2021-09-19 12:00:00',
    },
    {
        id: 20,
        fileName: 'Natural Langu...',
        createdAt: '2021-09-20 12:00:00',
    },
]);
const filteredFiles = computed(() => {
    return files.value;
});
</script>
<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">
                <h1 class="p-3 text-center text-2xl font-semibold md:mx-10 md:px-8">
                    Knowledge Stack : <span>(Course Name Here ...)</span>
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
                        <button class="rounded bg-gray-500 p-2 text-white hover:bg-gray-600">
                            Search
                        </button>

                        <button class="rounded bg-gray-500 p-2 px-3 text-white hover:bg-gray-600">
                            <img src="../../assets/images/add.svg" alt="add.svg" class="h-6 invert scale-125" />
                        </button>
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
                                        File Name
                                    </th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                    >
                                        Created At
                                    </th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                    >
                                        Actions
                                    </th>
                                </tr>
                            </thead>
                            <tbody class="divide-y bg-white">
                                <tr
                                    v-for="file in filteredFiles"
                                    :key="file.id"
                                    class="divide-x even:bg-gray-50"
                                >
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ file.id }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ file.fileName }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ file.createdAt }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <button class="rounded border p-1 hover:bg-gray-100">
                                            <img
                                                src="../../assets/images/delete.svg"
                                                alt="delete.svg"
                                                class="h-6"
                                            />
                                        </button>
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
