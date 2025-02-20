<script setup>
import DeleteIcon from '@/components/icons/DeleteIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import FileUploadModal from '@/components/ui/modal/FileUploadModal.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { computed, ref } from 'vue';
import BaseView from './BaseView.vue';

const headers = ref([
    { label: 'ID', key: 'id' },
    { label: 'File Name', key: 'fileName' },
    { label: 'Created At', key: 'createdAt' },
    { label: 'Actions', key: 'actions' },
]);

const files = ref([
    {
        id: 1,
        fileName: 'Software Eng...',
        createdAt: '2021-09-01 12:00:00',
    },
    {
        id: 2,
        fileName: 'Data Struct...',
        createdAt: '2021-09-02 12:00:00',
    },
    {
        id: 3,
        fileName: 'Operating Systems',
        createdAt: '2021-09-03 12:00:00',
    },
    {
        id: 4,
        fileName: 'Computer Networks',
        createdAt: '2021-09-04 12:00:00',
    },
    {
        id: 5,
        fileName: 'Database Mana...',
        createdAt: '2021-09-05 12:00:00',
    },
    {
        id: 6,
        fileName: 'Computer Archi...',
        createdAt: '2021-09-06 12:00:00',
    },
    {
        id: 7,
        fileName: 'Artificial Int...',
        createdAt: '2021-09-07 12:00:00',
    },
    {
        id: 8,
        fileName: 'Machine Learn...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 9,
        fileName: 'Machine Learn...',
        createdAt: '2021-09-08 12:00:00',
    },
    {
        id: 10,
        fileName: 'Natural Langu...',
        createdAt: '2021-09-10 12:00:00',
    },
    {
        id: 11,
        fileName: 'Software Eng...',
        createdAt: '2021-09-11 12:00:00',
    },
    {
        id: 12,
        fileName: 'Data Struct...',
        createdAt: '2021-09-12 12:00:00',
    },
    {
        id: 13,
        fileName: 'Operating Systems',
        createdAt: '2021-09-13 12:00:00',
    },
    {
        id: 14,
        fileName: 'Computer Networks',
        createdAt: '2021-09-14 12:00:00',
    },
    {
        id: 15,
        fileName: 'Database Mana...',
        createdAt: '2021-09-15 12:00:00',
    },
    {
        id: 16,
        fileName: 'Computer Archi...',
        createdAt: '2021-09-16 12:00:00',
    },
    {
        id: 17,
        fileName: 'Artificial Int...',
        createdAt: '2021-09-17 12:00:00',
    },
    {
        id: 18,
        fileName: 'Machine Learn...',
        createdAt: '2021-09-18 12:00:00',
    },
    {
        id: 19,
        fileName: 'Deep Learning',
        createdAt: '2021-09-19 12:00:00',
    },
    {
        id: 20,
        fileName: 'Natural Langu...',
        createdAt: '2021-09-20 12:00:00',
    },
]);

const filteredFiles = computed(() => {
    return files.value;
});

const isFileUploadModalOpen = ref(false);
const toggleFileUploadModal = () => {
    isFileUploadModalOpen.value = !isFileUploadModalOpen.value;
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
