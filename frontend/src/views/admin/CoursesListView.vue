<script setup>
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
                            <img
                                src="../../assets/images/add.svg"
                                alt="add.svg"
                                class="h-6 scale-125 invert"
                            />
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
                                    class="divide-x even:bg-gray-50"
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
                                                class="rounded border p-1 px-2 hover:bg-gray-100"
                                                :to="`/admin/enrollments?course_id=${course.id}`"
                                            >
                                                <img
                                                    src="../../assets/images/student.svg"
                                                    alt="student.svg"
                                                    class="h-6"
                                                />
                                            </RouterLink>
                                            <RouterLink
                                                class="rounded border p-1 px-2 hover:bg-gray-100"
                                                :to="`/admin/kstack?course_id=${course.id}`"
                                            >
                                                <img
                                                    src="../../assets/images/stack.svg"
                                                    alt="stack.svg"
                                                    class="h-6"
                                                />
                                            </RouterLink>
                                            <RouterLink
                                                class="rounded border p-1 px-2 hover:bg-gray-100"
                                                :to="`/course/${course.id}`"
                                            >
                                                <img
                                                    src="../../assets/images/view.png"
                                                    alt="view.png"
                                                    class="h-6"
                                                />
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
