<template>
    <svg
        v-if="isSolid"
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
    >
        <path
            fill="currentColor"
            d="M20.894 15.553a1 1 0 0 1-.447 1.341l-8 4a1 1 0 0 1-.894 0l-8-4a1 1 0 0 1 .894-1.788L12 18.88l7.554-3.775a1 1 0 0 1 1.341.447m0-4a1 1 0 0 1-.447 1.341l-8 4a1 1 0 0 1-.894 0l-8-4a1 1 0 0 1 .894-1.788L12 14.88l7.554-3.775a1 1 0 0 1 1.341.447M12.008 3q.056 0 .111.007l.111.02l.086.024l.012.006l.012.002l.029.014l.05.019l.016.009l.012.005l8 4a1 1 0 0 1 0 1.788l-8 4a1 1 0 0 1-.894 0l-8-4a1 1 0 0 1 0-1.788l8-4l.011-.005l.018-.01l.078-.032l.011-.002l.013-.006l.086-.024l.11-.02l.056-.005z"
            stroke-width="0.5"
            stroke="currentColor"
        />
    </svg>
    <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
        <path
            fill="none"
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 4L4 8l8 4l8-4zm-8 8l8 4l8-4M4 16l8 4l8-4"
        />
    </svg>
</template>

<script setup>
defineProps({
    isSolid: {
        type: Boolean,
        default: false,
    },
});
</script>
