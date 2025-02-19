<template>
    <div class="overflow-y-auto">
        <table class="w-full divide-y">
            <thead class="sticky top-0 bg-blue-500 shadow">
                <tr class="divide-x">
                    <th
                        v-for="header in headers"
                        :key="header.key"
                        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-white"
                    >
                        {{ header.label }}
                    </th>
                </tr>
            </thead>
            <tbody class="divide-y bg-white">
                <TableRow v-for="row in data" :key="row.id" :row="row" :headers="headers" />
            </tbody>
        </table>
    </div>
</template>

<script setup>
import TableRow from './TableRow.vue';

defineProps({
    headers: Array,
    data: Array,
});
</script>
