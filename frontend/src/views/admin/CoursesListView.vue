<script setup>
import EyeIcon from '@/components/icons/EyeIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import StackIcon from '@/components/icons/StackIcon.vue';
import StudentIcon from '@/components/icons/StudentIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { computed, ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import BaseView from './BaseView.vue';
import { getAllCourses } from '@/api';
import { push } from 'notivue';

const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'Course Name', key: 'name' },
    { label: 'Actions', key: 'actions' },
]);
const courses = ref([]);
const filteredCourses = computed(() => courses.value);

onMounted(() => {
    getAllCourses()
        .then((response) => {
            courses.value = response.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching courses !');
        });
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

                        <TableComponent :headers="headers" :rows="filteredCourses">
                            <template #actions="{ row }">
                                <div class="flex gap-2">
                                    <RouterLink :to="`/admin/enrollments?course_id=${row.id}`">
                                        <Button varient="light" :rounded="true">
                                            <StudentIcon class="h-6 w-6" />
                                        </Button>
                                    </RouterLink>
                                    <RouterLink :to="`/admin/kstack?course_id=${row.id}`">
                                        <Button varient="light" :rounded="true">
                                            <StackIcon class="h-6 w-6" />
                                        </Button>
                                    </RouterLink>
                                    <RouterLink :to="`/course/${row.id}`">
                                        <Button varient="light" :rounded="true">
                                            <EyeIcon class="h-6 w-6" />
                                        </Button>
                                    </RouterLink>
                                </div>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
