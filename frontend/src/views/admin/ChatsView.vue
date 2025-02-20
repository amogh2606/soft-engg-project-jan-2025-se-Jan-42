<script setup>
import ExportIcon from '@/components/icons/ExportIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import BaseView from '@/views/admin/BaseView.vue';
import { ref } from 'vue';

const headers = ref([
    { key: 'id', label: 'ID' },
    { key: 'query', label: 'Query' },
    { key: 'response', label: 'Response' },
]);
const chats = ref([
    { id: 1, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 2, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 3, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 4, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 5, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 6, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 7, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 8, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 9, query: 'Your Query ...?', response: 'Bot Response Here ...' },
    { id: 10, query: 'Your Query ...?', response: 'Bot Response Here ...' },
]);
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

                            <Button varient="primary">
                                <ExportIcon :is-solid="false" class="h-6 w-auto" />
                            </Button>
                        </div>
                        <TableComponent :headers="headers" :rows="chats" />
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
