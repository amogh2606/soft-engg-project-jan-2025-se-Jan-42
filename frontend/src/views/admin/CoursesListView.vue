<script setup>
import { getAllCourses } from '@/api';
import EyeIcon from '@/components/icons/EyeIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import StackIcon from '@/components/icons/StackIcon.vue';
import StudentIcon from '@/components/icons/StudentIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import AddCourseModal from '@/components/ui/modal/AddCourseModal.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { push } from 'notivue';
import { computed, ref, watch } from 'vue';
import { RouterLink } from 'vue-router';
import BaseView from './BaseView.vue';

const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'Course Name', key: 'name' },
    { label: 'Actions', key: 'actions' },
]);
const searchInput = ref('');
const courses = ref([]);
const filteredCourses = computed(() =>
    courses.value.filter((c) => c.name.toLowerCase().includes(searchInput.value?.toLowerCase())),
);
const isAddCourseModalOpen = ref(false);
const toggleAddCourseModal = () => {
    isAddCourseModalOpen.value = !isAddCourseModalOpen.value;
};

const fetchCourses = () => {
    getAllCourses()
        .then((response) => {
            courses.value = response.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching courses !');
        });
};

watch(
    isAddCourseModalOpen,
    () => {
        if (!isAddCourseModalOpen.value) {
            fetchCourses();
        }
    },
    { immediate: true },
);
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
                                v-model="searchInput"
                            />
                            <Button varient="primary">Search</Button>
                            <Button varient="primary" @click="toggleAddCourseModal">
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
                                    <RouterLink :to="`/course?course_id=${row.id}`">
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
            <AddCourseModal v-model="isAddCourseModalOpen" />
        </template>
    </BaseView>
</template>
