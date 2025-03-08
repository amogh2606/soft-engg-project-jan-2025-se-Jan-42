<script setup>
import {
    deleteDocumentFromKnowledgeStack,
    getCourseById,
    getKnowledgeStackByCourseId,
} from '@/api';
import DeleteIcon from '@/components/icons/DeleteIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import FileUploadModal from '@/components/ui/modal/FileUploadModal.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { push } from 'notivue';
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import BaseView from './BaseView.vue';

const courseId = useRoute().query.course_id;
const course = ref(null);
const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'File Name', key: 'fileName' },
    { label: 'Actions', key: 'actions' },
]);
const files = ref([]);
const filteredFiles = computed(() => files.value);

const isFileUploadModalOpen = ref(false);
const toggleFileUploadModal = () => {
    isFileUploadModalOpen.value = !isFileUploadModalOpen.value;
};

const deleteDocument = (fileName) => {
    deleteDocumentFromKnowledgeStack(courseId, fileName)
        .then((response) => {
            push.success('File deleted successfully');
            loadKnowledgeStack();
        })
        .catch((error) => {
            if (error?.response?.status === 404) {
                push.error('File not found !');
            } else {
                push.error(error?.response?.data?.message || 'Failed to delete file !');
            }
        });
};

const loadKnowledgeStack = () => {
    getKnowledgeStackByCourseId(courseId)
        .then((response) => {
            files.value = response.data.documents.map((file, index) => ({
                fileName: file,
                id: index + 1,
            }));
        })
        .catch((error) => {
            console.error(error);
            if (error?.response?.status === 404) {
                push.error('No knowledge stack found for this course !');
            } else {
                push.error(error?.response?.data?.message || 'Error fetching knowledge stack !');
            }
        });
};

onMounted(() => {
    getCourseById(courseId)
        .then((response) => {
            course.value = response.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching course !');
        });
});

watch(
    isFileUploadModalOpen,
    () => {
        if (!isFileUploadModalOpen.value) {
            loadKnowledgeStack();
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
                        Knowledge Stack : <span>{{ course?.name || 'Course Name Here ...' }}</span>
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                            />
                            <Button varient="primary">Search</Button>
                            <Button varient="primary" @click="toggleFileUploadModal">
                                <PlusIcon class="h-6 w-auto" />
                            </Button>
                        </div>

                        <TableComponent :headers="headers" :rows="filteredFiles">
                            <template #actions="{ row }">
                                <Button
                                    varient="outlineRed"
                                    :rounded="true"
                                    @click="deleteDocument(row.fileName)"
                                >
                                    <DeleteIcon :isSolid="false" class="h-6 w-auto" />
                                </Button>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
            <FileUploadModal v-model="isFileUploadModalOpen" :course-id="courseId?.toString()" />
        </template>
    </BaseView>
</template>
