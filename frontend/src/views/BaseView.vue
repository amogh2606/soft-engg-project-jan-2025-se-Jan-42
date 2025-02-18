<script setup>
import { Notification, NotificationProgress, Notivue } from 'notivue';
</script>

<template>
    <slot></slot>
    <Notivue v-slot="item">
        <Notification :item="item">
            <NotificationProgress :item="item" v-if="item.showProgress" />
        </Notification>
    </Notivue>
</template>

<style>
@import 'notivue/animations.css';
@import 'notivue/notification.css';
@import 'notivue/notification-progress.css';
</style>
