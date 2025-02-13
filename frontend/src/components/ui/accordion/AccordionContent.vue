<script setup>
import { inject, onBeforeUnmount, onMounted, ref } from 'vue';

const { id, isOpen } = inject('accordionItemContext');
const contentRef = ref(null);

// Add component name for validation
defineOptions({
    name: 'AccordionContent',
});

let resizeObserver;

onMounted(() => {
    if (!contentRef.value) return;

    resizeObserver = new ResizeObserver(() => {
        const element = contentRef.value;
        if (!element) return;

        if (isOpen.value) {
            element.style.maxHeight = element.scrollHeight + 'px';
        }
    });

    resizeObserver.observe(contentRef.value);
});

onBeforeUnmount(() => {
    if (resizeObserver) {
        resizeObserver.disconnect();
    }
});
</script>

<template>
    <div
        ref="contentRef"
        :id="'content-' + id"
        class="overflow-hidden transition-[max-height] duration-300 ease-in-out"
        :style="{ maxHeight: isOpen ? contentRef?.scrollHeight + 'px' : '0px' }"
        role="region"
        :aria-labelledby="'header-' + id"
    >
        <div class="px-6 pb-4">
            <slot></slot>
        </div>
    </div>
</template>
