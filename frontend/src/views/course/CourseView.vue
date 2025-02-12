<script setup>
import BaseView from './BaseView.vue';
</script>
<template>
    <BaseView>
        <template #right-slot>
            <div class="grid content-center w-full">
                <h1 class="text-2xl font-semibold text-center">Course Content</h1>
            </div>
        </template>
    </BaseView>
</template>
