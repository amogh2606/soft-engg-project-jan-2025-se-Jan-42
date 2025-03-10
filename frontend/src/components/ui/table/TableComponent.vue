<script setup>
defineProps({
    headers: {
        type: Array,
        required: true,
        // Validate that each header has key and label
        validator: (headers) =>
            headers.every(
                (header) => typeof header === 'object' && 'key' in header && 'label' in header,
            ),
    },
    rows: {
        type: Array,
        required: true,
    },
});
</script>

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
                <tr v-if="rows.length === 0">
                    <td colspan="100%" class="py-4 text-sm text-center">No data found !</td>
                </tr>
                <tr
                    v-else
                    v-for="(row, rowIndex) in rows"
                    :key="rowIndex"
                    class="cursor-pointer divide-x hover:bg-gray-50"
                >
                    <td
                        v-for="header in headers"
                        :key="header.key"
                        class="whitespace-nowrap px-6 py-4"
                    >
                        <!-- Check if a slot is provided for this column -->
                        <slot v-if="$slots[header.key]" :name="header.key" :row="row"></slot>
                        <div v-else class="text-sm text-gray-900">
                            {{ row[header.key] || 'N/A' }}
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
