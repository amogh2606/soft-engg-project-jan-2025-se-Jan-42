<script setup>
import { getAllCourses, getAllUsers } from '@/api';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import AddInstructorModal from '@/components/ui/modal/AddInstructorModal.vue';
import LinkCourseAndInstructorModal from '@/components/ui/modal/LinkCourseAndInstructorModal.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { push } from 'notivue';
import { computed, ref, watch } from 'vue';
import BaseView from './BaseView.vue';
const headers = ref([
    { label: 'Name', key: 'name' },
    { label: 'Email', key: 'email' },
    { label: 'Course', key: 'course' },
    { label: 'Actions', key: 'actions' },
]);

const courses = ref([]);
const selectedInstructor = ref(null);
const instructors = ref([]);
const filteredInstructors = computed(() => instructors.value);
const isAddInstructorModalOpen = ref(false);
const isLinkCourseModalOpen = ref(false);
const toggleAddInstructorModal = () => {
    isAddInstructorModalOpen.value = !isAddInstructorModalOpen.value;
};
const toggleLinkCourseModal = () => {
    isLinkCourseModalOpen.value = !isLinkCourseModalOpen.value;
};
const availableCourses = computed(() => {
    return courses.value.filter(
        (course) => !instructors.value.some((instructor) => instructor.course?.id === course.id),
    );
});

const fetchInstructors = () => {
    getAllCourses()
        .then((response) => {
            courses.value = response?.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching courses !');
        });
    getAllUsers('instructor')
        .then((response) => {
            instructors.value = response?.data?.map((instructor) => ({
                ...instructor,
                role: instructor.roles.at(0),
                course: instructor?.courses?.at(0) || null,
            }));
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching instructors !');
        });
};

watch(
    [isAddInstructorModalOpen, isLinkCourseModalOpen],
    () => {
        if (!isAddInstructorModalOpen.value && !isLinkCourseModalOpen.value) {
            fetchInstructors();
        }
    },
    { immediate: true },
);

const handleLinkCourse = (instructor) => {
    console.log('handleLinkCourse', instructor);
    selectedInstructor.value = instructor;
    toggleLinkCourseModal();
};
</script>

<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">
                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded-lg border bg-white p-4 shadow md:mx-10 md:mb-10"
                >
                    <h1 class="p-3 pb-7 text-center text-2xl font-semibold md:mx-10 md:px-8">
                        Instructors
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                            />
                            <Button varient="primary">Search</Button>

                            <Button varient="primary" @click="toggleAddInstructorModal">
                                <PlusIcon class="h-6 w-auto" />
                            </Button>
                        </div>
                        <TableComponent :headers="headers" :rows="filteredInstructors">
                            <template #course="{ row }">
                                <div class="text-sm text-gray-900">
                                    {{ row?.course?.name || 'N/A' }}
                                </div>
                            </template>
                            <template #actions="{ row }">
                                <Button
                                    :disabled="row?.course?.name ? true : false"
                                    varient="primary"
                                    class="!text-sm"
                                    @click="handleLinkCourse(row)"
                                    >Link Course</Button
                                >
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
            <AddInstructorModal v-model="isAddInstructorModalOpen" />
            <LinkCourseAndInstructorModal
                v-model="isLinkCourseModalOpen"
                :courses="availableCourses"
                :instructor="selectedInstructor"
            />
        </template>
    </BaseView>
</template>
