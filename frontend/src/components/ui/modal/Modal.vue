<template>
    <transition name="modal-fade">
        <div
            v-if="isOpen"
            class="fixed inset-0 z-50 flex items-center justify-center"
            tabindex="0"
            role="dialog"
            aria-modal="true"
        >
            <!-- Overlay without click event -->
            <div class="fixed inset-0 bg-black opacity-50"></div>
            <!-- Modal Container -->
            <div class="relative z-10 w-full max-w-lg rounded-lg bg-white p-6 shadow-xl">
                <!-- Optional Close Button -->
                <button
                    v-if="showCloseButton"
                    class="absolute right-3 top-3 text-gray-500 hover:text-gray-700 focus:outline-none"
                    @click="close"
                    aria-label="Close modal"
                >
                    <CrossIcon class="h-6 w-6" />
                </button>
                <div>
                    <slot></slot>
                </div>
            </div>
        </div>
    </transition>
</template>

<script setup>
import { computed, onUnmounted, watch } from 'vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';

defineOptions({
    name: 'AppModal',
});

const props = defineProps({
    modelValue: {
        type: Boolean,
        default: false,
    },
    showCloseButton: {
        type: Boolean,
        default: true,
    },
});

const emit = defineEmits(['update:modelValue', 'open', 'close']);

// Use computed for two-way binding with modelValue.
const isOpen = computed({
    get() {
        return props.modelValue;
    },
    set(value) {
        emit('update:modelValue', value);
        if (value) {
            emit('open');
        } else {
            emit('close');
        }
    },
});

function close() {
    isOpen.value = false;
}

function handleEsc(event) {
    if (event.key === 'Escape') {
        close();
    }
}

// Watch for changes in isOpen and attach/detach the keydown listener immediately.
watch(
    isOpen,
    (open) => {
        if (open) {
            document.addEventListener('keydown', handleEsc);
        } else {
            document.removeEventListener('keydown', handleEsc);
        }
    },
    { immediate: true },
);

// Ensure cleanup on component unmount.
onUnmounted(() => {
    document.removeEventListener('keydown', handleEsc);
});
</script>

<style scoped>
.modal-fade-enter-active,
.modal-fade-leave-active {
    transition: opacity 0.1s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
    opacity: 0;
}
</style>
