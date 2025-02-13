<script setup>
import ChevronDownIcon from '@/components/icons/ChevronDownIcon.vue';
import ChevronUpIcon from '@/components/icons/ChevronUpIcon.vue';
import { inject } from 'vue';

defineProps({
    title: {
        type: String,
        required: false,
    },
});

const accordionContext = inject('accordionContext');
const { id, isOpen } = inject('accordionItemContext');

// Add component name for validation
defineOptions({
    name: 'AccordionHeader',
});

const handleKeyDown = (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        accordionContext.togglePanel(id);
    }
};
</script>

<template>
    <button
        class="flex w-full items-center justify-between gap-2 px-6 py-4 text-left transition-colors hover:bg-gray-100 focus:outline-none"
        :class="{ 'bg-gray-100': isOpen }"
        @click="accordionContext.togglePanel(id)"
        @keydown="handleKeyDown"
        :aria-expanded="isOpen"
        :aria-controls="'content-' + id"
    >
        <slot>
            <span class="text-lg font-medium text-gray-900">{{ title }}</span>
        </slot>
        <component
            :is="isOpen ? ChevronUpIcon : ChevronDownIcon"
            class="h-5 w-5 text-gray-500"
            aria-hidden="true"
        />
    </button>
</template>
