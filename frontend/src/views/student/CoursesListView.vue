<script setup>
import { enrollUserInCourse, getAllCourses, getUser } from '@/api';
import EyeIcon from '@/components/icons/EyeIcon.vue';
import FeedbackIcon from '@/components/icons/FeedbackIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import SubmitFeedbackModal from '@/components/ui/modal/SubmitFeedbackModal.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { useAuthStore } from '@/stores/auth';
import { push } from 'notivue';
import { computed, onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';
import BaseView from './BaseView.vue';

const { user, setUser } = useAuthStore();
const activeTab = ref('enrolled');
const headers = ref([
    { label: 'Course Name', key: 'name' },
    { label: 'Actions', key: 'actions' },
]);
const searchInput = ref('');
const courses = ref([]);
const enrolledCourses = ref([]);
const filteredCourses = computed(() => {
    if (activeTab.value === 'enrolled') {
        return enrolledCourses.value.filter((c) =>
            c.name.toLowerCase().includes(searchInput.value?.toLowerCase()),
        );
    }
    return courses.value
        .filter((c) => !enrolledCourses.value.find((ec) => ec.id === c.id))
        .filter((c) => c.name.toLowerCase().includes(searchInput.value?.toLowerCase()));
});

const isFeedbackModalOpen = ref(false);
const courseIdForFeedback = ref('');

const toggleFeedbackModal = (courseId) => {
    courseIdForFeedback.value = courseId;
    isFeedbackModalOpen.value = !isFeedbackModalOpen.value;
};

const fetchCourses = () => {
    getUser()
        .then((response) => {
            enrolledCourses.value = response.data.courses;
            setUser(response.data);
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching courses !');
        });
    getAllCourses()
        .then((response) => {
            courses.value = response.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching courses !');
        });
};

onMounted(() => {
    fetchCourses();
});

const enrollInCourse = (userId, courseId) => {
    enrollUserInCourse(userId, courseId)
        .then((res) => {
            push.success('Course enrolled successfully');
            fetchCourses();
        })
        .catch((err) => {
            console.error(err);
            push.error('Failed to enroll in course');
        });
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
                        Student Courses
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex border-b">
                            <button
                                class="px-6 py-3 font-medium"
                                :class="{
                                    'border-b-2 border-blue-500 text-blue-500':
                                        activeTab === 'enrolled',
                                }"
                                @click="activeTab = 'enrolled'"
                            >
                                Enrolled Courses
                            </button>
                            <button
                                class="px-6 py-3 font-medium"
                                :class="{
                                    'border-b-2 border-blue-500 text-blue-500': activeTab === 'all',
                                }"
                                @click="activeTab = 'all'"
                            >
                                Pending Courses
                            </button>
                        </div>
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
                                <RouterLink
                                    v-if="enrolledCourses?.find((c) => c.id === row.id)"
                                    :to="`/course?course_id=${row.id}`"
                                >
                                    <Button varient="light" :rounded="true">
                                        <EyeIcon class="h-6 w-6" />
                                    </Button>
                                </RouterLink>
                                <Button
                                    v-else
                                    varient="light"
                                    :rounded="true"
                                    @click="enrollInCourse(user.id, row.id)"
                                >
                                    <PlusIcon class="h-6 w-6" />
                                </Button>
                                <Button
                                    v-if="enrolledCourses?.find((c) => c.id === row.id)"
                                    varient="light"
                                    :rounded="true"
                                    class="ml-2"
                                    @click="toggleFeedbackModal(row.id)"
                                >
                                    <FeedbackIcon class="h-6 w-6" />
                                </Button>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
            <SubmitFeedbackModal :course-id="courseIdForFeedback" v-model="isFeedbackModalOpen" />
        </template>
    </BaseView>
</template>
