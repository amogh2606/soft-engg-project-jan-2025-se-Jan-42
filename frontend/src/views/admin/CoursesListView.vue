<script setup>
import EyeIcon from '@/components/icons/EyeIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import StackIcon from '@/components/icons/StackIcon.vue';
import StudentIcon from '@/components/icons/StudentIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import { ref } from 'vue';
import BaseView from './BaseView.vue';

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
</script>
<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">
                <h1 class="p-3 text-center text-2xl font-semibold md:mx-10 md:px-8">Courses</h1>

                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded-lg border bg-white shadow md:mx-10 md:mb-10"
                >
                    <!-- search box -->
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
                                        Course Name
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
                                    v-for="course in courses"
                                    :key="course.id"
                                    class="cursor-pointer divide-x hover:bg-gray-50"
                                >
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ course.id }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ course.name }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="flex gap-2">
                                            <RouterLink
                                                :to="`/admin/enrollments?course_id=${course.id}`"
                                            >
                                                <Button varient="light">
                                                    <StudentIcon class="h-6 w-6" />
                                                </Button>
                                            </RouterLink>
                                            <RouterLink
                                                :to="`/admin/kstack?course_id=${course.id}`"
                                            >
                                                <Button varient="light">
                                                    <StackIcon class="h-6 w-6" />
                                                </Button>
                                            </RouterLink>
                                            <RouterLink :to="`/course/${course.id}`">
                                                <Button varient="light">
                                                    <EyeIcon class="h-6 w-6" />
                                                </Button>
                                            </RouterLink>
                                        </div>
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
