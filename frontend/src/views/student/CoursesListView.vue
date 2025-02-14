<script setup>
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
        <template #right-slot>
            <div class="flex h-full flex-1 flex-col items-center justify-center gap-4">
                <h1 class="mt-4 text-2xl font-bold">Enrolled Courses</h1>
                <div v-if="courses.length === 0" class="text-xl text-gray-600">
                    No courses available !
                </div>
                <div v-else class="my-4 flex flex-wrap justify-center gap-4 overflow-y-scroll">
                    <div
                        v-for="course in courses"
                        :key="course.id"
                        class="custom flex aspect-square w-52 flex-col items-center justify-between rounded border border-gray-300 text-center hover:bg-gray-300 hover:shadow"
                    >
                        <p class="my-auto px-2 text-xl font-semibold text-white">
                            {{ course.name }}
                        </p>

                        <RouterLink :to="'/course/' + course.id" class="w-full">
                            <Button class="mt-2 w-full rounded-none" varient="light"
                                >View Course</Button
                            >
                        </RouterLink>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>

<style scoped>
.custom {
    background-image: url('../../assets/images/course-thumbnail.svg');
}
</style>
