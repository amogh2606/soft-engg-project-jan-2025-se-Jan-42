<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <button
        :class="[
            rounded ? roundedBaseClasses : baseClasses,
            btnVarients[varient],
            { 'cursor-not-allowed opacity-50': disabled },
            { 'flex items-center justify-center gap-2': loading },
        ]"
        :disabled="disabled"
    >
        <SpinnerIcon v-if="loading" variant="primary" class="animate-spin" />
        <slot></slot>
    </button>
</template>

<script setup>
import SpinnerIcon from '@/components/icons/SpinnerIcon.vue';

const baseClasses = 'px-4 py-2 rounded cursor-pointer transition-colors font-medium';
const roundedBaseClasses = 'rounded-full p-1.5 cursor-pointer transition-colors font-medium';
const btnVarients = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600',
    secondary: 'bg-gray-500 text-white hover:bg-gray-600',
    light: 'bg-white border border-gray-400 text-gray-500 hover:bg-gray-100 hover:text-gray-700',
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
                value,
            ),
    },
    rounded: {
        type: Boolean,
        default: false,
    },
    disabled: {
        type: Boolean,
        default: false,
    },
    loading: {
        type: Boolean,
        default: false,
    },
});
</script>

<style scoped></style>
