<template>
    <div class="grid flex-1 content-center overflow-y-scroll bg-gray-50">
        <div class="flex flex-col items-center justify-center">
            <h1 class="text-2xl font-semibold">Course Overview</h1>
            <p class="text-gray-500">{{ course?.description }}</p>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    course: {
        type: Object,
        required: false,
    },
});
</script>
