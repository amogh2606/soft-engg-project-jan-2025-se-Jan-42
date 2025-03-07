<script setup>
import { getKnowledgeStackByCourseId } from '@/api';
import DeleteIcon from '@/components/icons/DeleteIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import FileUploadModal from '@/components/ui/modal/FileUploadModal.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { useAuthStore } from '@/stores/auth';
import { push } from 'notivue';
import { computed, onMounted, ref } from 'vue';
import BaseView from './BaseView.vue';

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

onMounted(() => {
    const { courseIdOfInstructor } = useAuthStore();
    getKnowledgeStackByCourseId(courseIdOfInstructor)
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
                push.error('Error fetching knowledge stack !');
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
                        Knowledge Stack
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
                                <Button varient="outlineRed" :rounded="true">
                                    <DeleteIcon :isSolid="false" class="h-6 w-auto" />
                                </Button>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
            <FileUploadModal v-model="isFileUploadModalOpen" />
        </template>
    </BaseView>
</template>
