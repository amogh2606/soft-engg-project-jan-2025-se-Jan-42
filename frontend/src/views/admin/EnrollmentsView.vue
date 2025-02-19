<script setup lang="jsx">
import DeleteIcon from '@/components/icons/DeleteIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';

const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'Student Name', key: 'name' },
    { label: 'Created At', key: 'createdAt' },
    { label: 'Actions', key: 'actions' },
]);

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

students.value.forEach((student) => {
    student.actions = {
        render: () => (
            <Button varient="outlineRed" rounded="true">
                <DeleteIcon isSolid="false" class="h-6 w-auto" />
            </Button>
        ),
    };
});

const filteredStudents = computed(() => {
    return students.value;
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
                        Manage Enrollments : <span>(Course Name Here ...)</span>
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                            />
                            <Button varient="primary">Search</Button>
                            <Button varient="primary">
                                <PlusIcon class="h-6 w-auto" />
                            </Button>
                        </div>
                        <TableComponent :headers="headers" :data="filteredStudents" />
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
