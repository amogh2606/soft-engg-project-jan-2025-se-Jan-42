<script setup>
import { provide, ref } from 'vue';
import ErrorBoundary from './ErrorBoundary.vue';

const props = defineProps({
    allowMultiple: {
        type: Boolean,
        default: false,
    },
    class: {
        type: String,
        default: '',
    },
});

const openPanels = ref(new Set());

const togglePanel = (id) => {
    if (props.allowMultiple) {
        if (openPanels.value.has(id)) {
            openPanels.value.delete(id);
        } else {
            openPanels.value.add(id);
        }
    } else {
        if (openPanels.value.has(id)) {
            openPanels.value.clear();
        } else {
            openPanels.value.clear();
            openPanels.value.add(id);
        }
    }
};

provide('accordionContext', {
    openPanels,
    togglePanel,
});
</script>

<template>
    <div class="w-full divide-y divide-gray-200" :class="props.class">
        <ErrorBoundary>
            <slot></slot>
        </ErrorBoundary>
    </div>
</template>
