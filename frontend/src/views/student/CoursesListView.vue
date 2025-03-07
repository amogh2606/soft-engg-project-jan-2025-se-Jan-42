<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import { useAuthStore } from '@/stores/auth';
import { onMounted, ref } from 'vue';
import BaseView from './BaseView.vue';
const courses = ref([]);

onMounted(() => {
    const { userCourses } = useAuthStore();
    courses.value = userCourses;
});
</script>
<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col justify-center overflow-hidden pt-4">
                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded-lg border bg-white p-4 shadow md:mx-10 md:mb-10"
                >
                    <h1 class="p-3 pb-7 text-center text-2xl font-semibold md:mx-10 md:px-8">
                        Enrolled Courses
                    </h1>
                    <div v-if="courses.length === 0" class="text-center text-xl text-gray-600">
                        No courses available !
                    </div>
                    <div
                        v-else
                        class="custom-grid w-full overflow-y-scroll rounded-lg border px-1 py-4 shadow"
                    >
                        <div
                            v-for="course in courses"
                            :key="course.id"
                            class="custom flex aspect-square w-52 flex-col items-center justify-between rounded-lg border border-gray-300 text-center shadow hover:bg-gray-300 hover:shadow-md"
                        >
                            <p class="my-auto px-2 text-xl font-semibold text-white">
                                {{ course.name }}
                            </p>

                            <RouterLink :to="'/course/' + course.id" class="w-full">
                                <Button class="mt-2 w-full rounded-b-lg" varient="light"
                                    >View Course</Button
                                >
                            </RouterLink>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>

<style scoped>
.custom {
    background-image: url('../../assets/images/course-thumbnail.svg');
    background-color: #e7e7ef;
    opacity: 0.8;
    background-image:
        repeating-radial-gradient(circle at 0 0, transparent 0, #e7e7ef 10px),
        repeating-linear-gradient(#444cf755, #444cf7);
    background-blend-mode: multiply;
}
.custom-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(min(200px, 100%), 1fr));
    place-items: center;
    gap: 1rem;
}
</style>
