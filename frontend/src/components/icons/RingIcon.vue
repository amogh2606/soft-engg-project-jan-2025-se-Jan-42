<template>
    <svg
        v-if="isSolid"
        xmlns="http://www.w3.org/2000/svg"
        width="48"
        height="48"
        viewBox="0 0 48 48"
    >
        <g fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="4">
            <path
                stroke-linecap="round"
                d="M43.776 20.994c-1.303-8.638-8.13-15.466-16.768-16.77m-6.032.003C11.366 5.685 4 13.982 4 24c0 10.02 7.37 18.32 16.986 19.774a20.2 20.2 0 0 0 6.018.002C35.646 42.474 42.476 35.643 43.776 27"
            />
            <path fill="currentColor" d="M24 16a8 8 0 1 0 0 16a8 8 0 0 0 0-16Z" />
        </g>
    </svg>
    <svg v-else xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48">
        <g fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="4">
            <path
                stroke-linecap="round"
                d="M43.776 20.994c-1.303-8.638-8.13-15.466-16.768-16.77m-6.032.003C11.366 5.685 4 13.982 4 24c0 10.02 7.37 18.32 16.986 19.774a20.2 20.2 0 0 0 6.018.002C35.646 42.474 42.476 35.643 43.776 27"
            />
            <path d="M24 16a8 8 0 1 0 0 16a8 8 0 0 0 0-16Z" />
        </g>
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
