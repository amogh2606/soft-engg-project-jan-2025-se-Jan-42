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
            fill-rule="evenodd"
            d="M3.291 3.309a.75.75 0 0 0-.976.996l3.093 6.945H13a.75.75 0 0 1 0 1.5H5.408l-3.093 6.945a.75.75 0 0 0 .976.996l19-8a.75.75 0 0 0 0-1.382z"
            clip-rule="evenodd"
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
            stroke-width="1.5"
            d="M22 12L3 20l3.563-8L3 4zM6.5 12H22"
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
