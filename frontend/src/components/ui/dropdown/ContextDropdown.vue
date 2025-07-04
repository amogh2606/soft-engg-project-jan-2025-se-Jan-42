<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="relative" ref="dropdown">
        <button
            class="flex items-center justify-center gap-1 rounded-md border p-1 px-2 hover:bg-gray-100"
            @click="isOpen = !isOpen"
            :class="{
                'bg-gray-100': selectedOption,
            }"
        >
            <ContextIcon :is-solid="selectedOption ? true : false" class="h-5 w-auto" />
            <span class="text-sm">
                {{ selectedOption || 'Course Context' }}
            </span>
        </button>
        <div
            v-if="isOpen && options.length > 0"
            class="absolute bottom-9 left-0 flex w-48 flex-col gap-1 rounded-lg border bg-white p-2 text-sm shadow"
        >
            <button
                v-for="option in options"
                :key="option"
                class="rounded-lg border p-1 px-2 text-left hover:bg-gray-100"
                :class="{
                    'bg-gray-300': selectedOption === option,
                    'hover:bg-gray-300': selectedOption === option,
                }"
                @click="updateSelectedOption(option)"
            >
                <div class="flex items-center gap-2">
                    <div
                        class="h-2 w-2 rounded-full"
                        :class="{
                            'bg-green-500': selectedOption === option,
                            'border border-gray-500': selectedOption !== option,
                        }"
                    ></div>
                    <span>{{ option }}</span>
                </div>
            </button>
        </div>
    </div>
</template>

<script setup>
import ContextIcon from '@/components/icons/ContextIcon.vue';
import { onMounted, onUnmounted, ref, watchEffect } from 'vue';

const props = defineProps({
    options: {
        type: Array,
        required: true,
    },
    modelValue: {
        type: [String, null],
        required: true,
    },
    closeOnSelect: {
        type: Boolean,
        default: true,
    },
});

const emit = defineEmits(['update:modelValue']);

const isOpen = ref(false);
const selectedOption = ref(props.modelValue);
const dropdown = ref(null);

watchEffect(() => {
    selectedOption.value = props.modelValue;
});

const updateSelectedOption = (option) => {
    selectedOption.value = option;
    emit('update:modelValue', option);
    if (props.closeOnSelect) {
        isOpen.value = false;
    }
};

const handleClickOutside = (event) => {
    if (!dropdown.value.contains(event.target) && isOpen.value) {
        isOpen.value = false;
    }
};

onMounted(() => {
    document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>
