<template>
    <div class="accordion" :class="className">
        <slot />
    </div>
</template>

<script setup>
import { provide, ref, watch } from 'vue';

const props = defineProps({
    allowMultiple: {
        type: Boolean,
        default: false,
    },
    defaultExpanded: {
        type: Array,
        default: () => [],
    },
    className: {
        type: String,
        default: '',
    },
});
const emit = defineEmits(['update:openItems']);

const openItems = ref(props.defaultExpanded);

watch(
    () => openItems.value,
    (newValue) => {
        emit('update:openItems', newValue);
    },
    { deep: true },
);

watch(
    () => props.defaultExpanded,
    (newValue) => {
        openItems.value = newValue;
    },
);

const toggleItem = (index) => {
    if (props.allowMultiple) {
        openItems.value = openItems.value.includes(index)
            ? openItems.value.filter((i) => i !== index)
            : [...openItems.value, index];
    } else {
        openItems.value = openItems.value.includes(index) ? [] : [index];
    }
};

// Provide state and toggle function to child components.
provide('toggleItem', toggleItem);
provide('openItems', openItems);
</script>
