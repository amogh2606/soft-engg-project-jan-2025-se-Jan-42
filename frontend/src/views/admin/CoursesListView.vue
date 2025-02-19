<!-- Todo: Fix this file to use the new table component, actions are not working -->
<script setup lang="jsx">
import EyeIcon from '@/components/icons/EyeIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import StackIcon from '@/components/icons/StackIcon.vue';
import StudentIcon from '@/components/icons/StudentIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { h, ref } from 'vue';
import { RouterLink } from 'vue-router';
import BaseView from './BaseView.vue';

const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'Course Name', key: 'name' },
    { label: 'Actions', key: 'actions' },
]);

const courses = ref([
    { id: 1, name: 'Software Engineering' },
    { id: 2, name: 'Data Structures and Algorithms' },
    { id: 3, name: 'Operating Systems' },
    { id: 4, name: 'Computer Networks' },
    { id: 5, name: 'Database Management Systems' },
    { id: 6, name: 'Computer Architecture' },
    { id: 7, name: 'Artificial Intelligence' },
    { id: 8, name: 'Machine Learning' },
    { id: 9, name: 'Deep Learning' },
    { id: 10, name: 'Natural Language Processing' },
]);

courses.value.forEach((course) => {
    course.actions = {
        key: 'actions',
        title: 'Actions',
        render: (_, record) => {
            return h('div', { class: 'flex gap-2' }, [
                h(RouterLink, { to: `/admin/enrollments?course_id=${record.id}` }, () => [
                    h(Button, { varient: 'light', rounded: true }, () => [
                        h(StudentIcon, { class: 'h-6 w-6' }),
                    ]),
                ]),
                h(RouterLink, { to: `/admin/kstack?course_id=${record.id}` }, () => [
                    h(Button, { varient: 'light', rounded: true }, () => [
                        h(StackIcon, { class: 'h-6 w-6' }),
                    ]),
                ]),
                h(RouterLink, { to: `/course/${record.id}` }, () => [
                    h(Button, { varient: 'light', rounded: true }, () => [
                        h(EyeIcon, { class: 'h-6 w-6' }),
                    ]),
                ]),
            ]);
        },
    };
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
                        Courses
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

                        <TableComponent :headers="headers" :data="courses" />
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
