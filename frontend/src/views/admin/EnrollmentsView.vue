<script setup>
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';
import Button from '@/components/ui/buttons/Button.vue';

const students = ref([
    {
        id: 1,
        name: 'Student Name Here ...',
        createdAt: '2021-09-01 12:00:00',
    },
    {
        id: 2,
        name: 'Student Name Here ...',
        createdAt: '2021-09-02 12:00:00',
    },
    {
        id: 3,
        name: 'Student Name Here ...',
        createdAt: '2021-09-03 12:00:00',
    },
    {
        id: 4,
        name: 'Student Name Here ...',
        createdAt: '2021-09-04 12:00:00',
    },
    {
        id: 5,
        name: 'Student Name Here ...',
        createdAt: '2021-09-05 12:00:00',
    },
    {
        id: 6,
        name: 'Student Name Here ...',
        createdAt: '2021-09-06 12:00:00',
    },
    {
        id: 7,
        name: 'Student Name Here ...',
        createdAt: '2021-09-07 12:00:00',
    },
    {
        id: 8,
        name: 'Student Name Here ...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 9,
        name: 'Student Name Here ...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 10,
        name: 'Student Name Here ...',
        createdAt: '2021-09-10 12:00:00',
    },
    {
        id: 11,
        name: 'Student Name Here ...',
        createdAt: '2021-09-11 12:00:00',
    },
    {
        id: 12,
        name: 'Student Name Here ...',
        createdAt: '2021-09-12 12:00:00',
    },
    {
        id: 13,
        name: 'Student Name Here ...',
        createdAt: '2021-09-13 12:00:00',
    },
    {
        id: 14,
        name: 'Student Name Here ...',
        createdAt: '2021-09-14 12:00:00',
    },
    {
        id: 15,
        name: 'Student Name Here ...',
        createdAt: '2021-09-15 12:00:00',
    },
    {
        id: 16,
        name: 'Student Name Here ...',
        createdAt: '2021-09-16 12:00:00',
    },
    {
        id: 17,
        name: 'Student Name Here ...',
        createdAt: '2021-09-17 12:00:00',
    },
    {
        id: 18,
        name: 'Student Name Here ...',
        createdAt: '2021-09-18 12:00:00',
    },
    {
        id: 19,
        name: 'Student Name Here ...',
        createdAt: '2021-09-19 12:00:00',
    },
    {
        id: 20,
        name: 'Student Name Here ...',
        createdAt: '2021-09-20 12:00:00',
    },
]);
const filteredStudents = computed(() => {
    return students.value;
});
</script>
<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">
                <h1 class="p-3 text-center text-2xl font-semibold md:mx-10 md:px-8">
                    Manage Enrollments : <span>(Course Name Here ...)</span>
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
                        <Button varient="primary">+</Button>
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
                                        Student Name
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
                                    v-for="student in filteredStudents"
                                    :key="student.id"
                                    class="divide-x even:bg-gray-50"
                                >
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ student.id }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ student.name }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ student.createdAt }}</div>
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
