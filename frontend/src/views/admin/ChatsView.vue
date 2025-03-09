<script setup>
import { getAllChats } from '@/api';
import ExportIcon from '@/components/icons/ExportIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import EyeIcon from '@/components/icons/EyeIcon.vue';
import BaseView from '@/views/admin/BaseView.vue';
import { push } from 'notivue';
import { computed, onMounted, ref } from 'vue';

const headers = [
    { key: 'id', label: 'Id' },
    { key: 'title', label: 'Title' },
    { key: 'created', label: 'Created At' },
    { key: 'actions', label: 'Actions' },
];
const chats = ref([]);
const filteredChats = computed(() => chats.value);

onMounted(() => {
    getAllChats()
        .then((response) => {
            chats.value = response.data;
        })
        .catch((error) => {
            console.error(error);
            push.error('Error fetching chats !');
        });
});

const downloadChats = () => {
    getAllChats(true)
        .then((response) => {
            // save as csv
            const blob = new Blob([response.data], { type: 'text/csv' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'chats.csv';
            a.click();
            push.success('Chats downloaded successfully !');
        })
        .catch((error) => {
            console.error(error);
            push.error('Error downloading chats !');
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
                        ChatBot Conversations
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                            />
                            <Button varient="primary">Search</Button>

                            <Button varient="primary" @click="downloadChats">
                                <ExportIcon :is-solid="false" class="h-6 w-auto" />
                            </Button>
                        </div>
                        <TableComponent :headers="headers" :rows="filteredChats">
                            <template #actions="{ row }">
                                <Button
                                    varient="light"
                                    :rounded="true"
                                    @click="openChat(row.id)"
                                >
                                    <EyeIcon :is-solid="false" class="h-6 w-6" />
                                </Button>
                            </template>
                        </TableComponent>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
