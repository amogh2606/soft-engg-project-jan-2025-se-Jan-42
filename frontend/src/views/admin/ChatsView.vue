<script setup>
import { ref } from 'vue';
import BaseView from './BaseView.vue';
import Button from '@/components/ui/buttons/Button.vue';
import ExportIcon from '@/components/icons/ExportIcon.vue';

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
                <h1 class="p-3 text-center text-2xl font-semibold md:mx-10 md:px-8">
                    ChatBot Conversations
                </h1>

                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded border bg-gray-50 shadow md:mx-10 md:mb-10"
                >
                    <!-- search box -->
                    <div class="flex justify-between gap-2 p-3">
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

                    <!-- Wrap the table in a scrollable container -->
                    <div class="overflow-y-auto">
                        <table class="w-full divide-y">
                            <thead class="sticky top-0 bg-yellow-50 shadow">
                                <tr class="divide-x">
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                    >
                                        Id
                                    </th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                    >
                                        Query
                                    </th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500"
                                    >
                                        Response
                                    </th>
                                </tr>
                            </thead>
                            <tbody class="divide-y bg-white">
                                <tr
                                    v-for="chat in chats"
                                    :key="chat.id"
                                    class="divide-x even:bg-gray-50"
                                >
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ chat.id }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ chat.query }}</div>
                                    </td>
                                    <td class="whitespace-nowrap px-6 py-4">
                                        <div class="text-sm text-gray-900">{{ chat.response }}</div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
