<script setup>
import { getUser } from '@/api';
import EyeIcon from '@/components/icons/EyeIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { useAuthStore } from '@/stores/auth';
import { push } from 'notivue';
import { computed, onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';
import BaseView from './BaseView.vue';

const { setUser } = useAuthStore();
const headers = ref([
    { label: 'Course Name', key: 'name' },
    { label: 'Actions', key: 'actions' },
]);
const searchInput = ref('');
const courses = ref([]);
const filteredCourses = computed(() =>
    courses.value.filter((c) => c.name.toLowerCase().includes(searchInput.value?.toLowerCase())),
);

const fetchCourses = () => {
    getUser()
        .then((response) => {
            courses.value = response.data.courses;
            setUser(response.data);
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching courses !');
        });
};

onMounted(() => {
    fetchCourses();
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
                        My Courses
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
                        </div>

                        <TableComponent :headers="headers" :rows="filteredCourses">
                            <template #actions="{ row }">
                                <RouterLink :to="`/course?course_id=${row.id}`">
                                    <Button varient="light" :rounded="true">
                                        <EyeIcon class="h-6 w-6" />
                                    </Button>
                                </RouterLink>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
