<script setup>
import { computed, inject, onMounted, provide, useSlots } from 'vue';

const props = defineProps({
    id: {
        type: String,
        required: true,
    },
});

const slots = useSlots();

onMounted(() => {
    const children = slots.default?.();

    if (!children) {
        throw new Error(
            'AccordionItem must contain both AccordionHeader and AccordionContent components',
        );
    }

    const hasHeader = children.some((child) => child.type?.name === 'AccordionHeader');
    const hasContent = children.some((child) => child.type?.name === 'AccordionContent');

    if (!hasHeader || !hasContent) {
        throw new Error(
            `AccordionItem requires both AccordionHeader and AccordionContent components. ${
                !hasHeader ? 'Missing AccordionHeader. ' : ''
            }${!hasContent ? 'Missing AccordionContent. ' : ''}`,
        );
    }
});

const accordionContext = inject('accordionContext');
const isOpen = computed(() => accordionContext.openPanels.value.has(props.id));

provide('accordionItemContext', {
    id: props.id,
    isOpen,
});
</script>

<template>
    <div class="border-b border-gray-200 last:border-b-0">
        <slot></slot>
    </div>
</template>
