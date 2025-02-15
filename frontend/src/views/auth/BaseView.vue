<script setup>
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import { RouterLink } from 'vue-router';
</script>
<template>
    <div class="flex h-screen w-screen flex-col">
        <header class="flex items-center justify-between border-b px-4 py-2">
            <RouterLink to="/">
                <IITMLogoIcon class="h-12" />
            </RouterLink>
        </header>
        <slot name="main-slot"></slot>
    </div>
</template>
