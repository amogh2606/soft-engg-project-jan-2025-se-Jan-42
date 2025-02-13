<template>
    <div class="border min-w-52" :class="{ 'bg-gray-100': isOpen }">
        <div class="flex items-center justify-between p-2 cursor-pointer" @click="handleToggle">
            <slot name="header" />
            <slot name="icon-open" v-if="isOpen">
                <img src="../../../assets/images/arrow-down.svg" alt="arrow-down.svg" class="h-6 rotate-180" />
            </slot>
            <slot name="icon-close" v-if="!isOpen">
                <img src="../../../assets/images/arrow-down.svg" alt="arrow-down.svg" class="h-6" />
            </slot>
        </div>
        <div class="p-2 px-4" v-if="isOpen">
            <slot name="body" />
        </div>
    </div>
</template>

<script setup>
import { computed, inject } from 'vue';

// Expect an index prop to identify this item.
const props = defineProps({
    index: {
        type: Number,
        required: true,
    },
});

const toggleItem = inject('toggleItem');
const openItems = inject('openItems');

const isOpen = computed(() => openItems.value.includes(props.index));

const handleToggle = () => {
    toggleItem(props.index);
};
</script>
