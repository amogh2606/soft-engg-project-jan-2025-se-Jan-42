<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <button :class="`${baseClasses} ${btnVarients[varient]}`">
        <slot></slot>
    </button>
</template>

<script setup>
const baseClasses = 'px-4 py-2 rounded cursor-pointer transition-colors font-medium';
const btnVarients = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600',
    secondary: 'bg-gray-500 text-white hover:bg-gray-600',
    light: 'bg-white border border-gray-200 text-gray-500 hover:bg-gray-100 hover:text-gray-700',
    outlineBlack: 'rounded border border-black text-black hover:bg-black hover:text-white',
    outlineBlue: 'rounded border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white',
    outlineRed: 'rounded border border-red-500 text-red-500 hover:bg-red-500 hover:text-white',
};

defineProps({
    varient: {
        type: String,
        default: 'primary',
        validator: (value) =>
            ['primary', 'secondary', 'light', 'outlineBlack', 'outlineBlue', 'outlineRed'].includes(
                value
            ),
    },
});
</script>

<style scoped></style>
