<template>
    <tr class="cursor-pointer divide-x hover:bg-gray-50">
        <td v-for="header in headers" :key="header.key" class="whitespace-nowrap px-6 py-4">
            <component v-if="isJSXComponent(row[header.key])" :is="row[header.key]" />
            <div v-else class="text-sm text-gray-900">{{ row[header.key] || 'N/A' }}</div>
        </td>
    </tr>
</template>

<script setup lang="jsx">
const isJSXComponent = (value) => {
    return typeof value === 'object' && value?.render !== undefined;
};

defineProps({
    row: Object,
    headers: Array,
});
</script>
