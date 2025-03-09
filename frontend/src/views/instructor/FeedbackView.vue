<script setup>
import { getFeedbacksByCourseId } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { useAuthStore } from '@/stores/auth';
import { push } from 'notivue';
import { computed, onMounted, ref } from 'vue';
import BaseView from './BaseView.vue';

const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'Title', key: 'title' },
    { label: 'Feedback', key: 'text' },
    { label: 'Created At', key: 'created' },
]);

const searchInput = ref('');
const feedbacks = ref([]);
const filteredFeedbacks = computed(() => {
    return feedbacks.value.filter(
        (feedback) =>
            feedback.title.toLowerCase().includes(searchInput.value?.toLowerCase()) ||
            feedback.text.toLowerCase().includes(searchInput.value?.toLowerCase()),
    );
});

onMounted(() => {
    const { courseIdOfInstructor } = useAuthStore();
    getFeedbacksByCourseId(courseIdOfInstructor)
        .then((response) => {
            feedbacks.value = response.data;
        })
        .catch((error) => {
            console.error(error);
            if (error?.response?.status === 404) {
                push.error('No feedbacks found for this course !');
            } else {
                push.error('Error fetching feedbacks !');
            }
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
                        Student Feedbacks
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
                        <TableComponent :headers="headers" :rows="filteredFeedbacks" />
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
