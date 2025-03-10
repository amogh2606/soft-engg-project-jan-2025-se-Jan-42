<template>
    <Transition name="fade">
        <div
            v-if="show"
            class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
        >
            <div class="flex flex-col items-center space-y-4">
                <div
                    class="border-primary h-12 w-12 animate-spin rounded-full border-4 border-t-transparent"
                ></div>
                <p v-if="message" class="text-lg font-medium text-white">
                    {{ message }}
                </p>
            </div>
        </div>
    </Transition>
</template>

<script setup>
defineProps({
    show: {
        type: Boolean,
        default: false,
    },
    message: {
        type: String,
        default: '',
    },
});
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
