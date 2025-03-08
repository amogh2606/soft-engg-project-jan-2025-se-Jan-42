<script setup>
import { getCourseById, getCourseEnrollments } from '@/api';
import DeleteIcon from '@/components/icons/DeleteIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import AddInstructorModal from '@/components/ui/modal/AddInstructorModal.vue';
import { push } from 'notivue';
import { computed, onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import BaseView from './BaseView.vue';

const courseId = useRoute().query.course_id;
const course = ref(null);
const headers = ref([
    { label: 'Name', key: 'name' },
    { label: 'Email', key: 'email' },
    { label: 'Role', key: 'role' },
    { label: 'Actions', key: 'actions' },
]);

const users = ref([]);
const activeTab = ref('student');

const filteredUsers = computed(() => {
    return users.value.filter((user) => user.role === activeTab.value);
});

const isAddInstructorModalOpen = ref(false);
const toggleAddInstructorModal = () => {
    isAddInstructorModalOpen.value = !isAddInstructorModalOpen.value;
};

onMounted(() => {
    getCourseById(courseId)
        .then((response) => {
            course.value = response?.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching course !');
        });
    getCourseEnrollments(courseId)
        .then((response) => {
            const { instructors, students } = response?.data?.enrolled_users?.reduce(
                (acc, user) => {
                    acc[user.roles.at(0) === 'instructor' ? 'instructors' : 'students'].push({
                        ...user,
                        role: user.roles.at(0),
                    });
                    return acc;
                },
                { instructors: [], students: [] },
            );
            users.value = [...instructors, ...students];
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching course enrollments !');
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
                        Manage Enrollments :
                        <span>{{ course?.name || 'Course Name Here ...' }}</span>
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex border-b">
                            <button
                                class="px-6 py-3 font-medium"
                                :class="{
                                    'border-b-2 border-blue-500 text-blue-500':
                                        activeTab === 'student',
                                }"
                                @click="activeTab = 'student'"
                            >
                                Students
                            </button>
                            <button
                                class="px-6 py-3 font-medium"
                                :class="{
                                    'border-b-2 border-blue-500 text-blue-500':
                                        activeTab === 'instructor',
                                }"
                                @click="activeTab = 'instructor'"
                            >
                                Instructors
                            </button>
                        </div>

                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                            />
                            <Button varient="primary">Search</Button>
                            <Button
                                v-if="activeTab === 'instructor' && filteredUsers.length === 0"
                                varient="primary"
                                @click="toggleAddInstructorModal"
                            >
                                <PlusIcon class="h-6 w-auto" />
                            </Button>
                        </div>
                        <TableComponent :headers="headers" :rows="filteredUsers">
                            <template #actions="{ row }">
                                <Button varient="outlineRed" :rounded="true">
                                    <DeleteIcon :isSolid="false" class="h-6 w-auto" />
                                </Button>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
            <AddInstructorModal v-model="isAddInstructorModalOpen" :course="course" />
        </template>
    </BaseView>
</template>
