<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <button :class="`${baseClasses} ${btnVarients[btnType]}`">
        <slot></slot>
    </button>
</template>

<script setup>
defineProps({
    btnType: {
        type: String,
        default: 'primary',
        validator: (value) => ['primary', 'secondary'].includes(value),
    },
});

const baseClasses = 'px-4 py-2 rounded cursor-pointer transition-colors font-medium';
const btnVarients = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600',
    secondary: 'bg-white border border-gray-300 text-gray-700 hover:bg-gray-50 hover:text-gray-800',
};
</script>

<style scoped></style>
