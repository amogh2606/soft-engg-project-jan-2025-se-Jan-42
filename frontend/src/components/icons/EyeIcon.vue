<template>
    <svg
        v-if="isSolid"
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        viewBox="0 0 16 16"
    >
        <path
            fill="currentColor"
            fill-rule="evenodd"
            d="m14.5 8l.415-.208V7.79l-.003-.003l-.006-.012l-.021-.04l-.08-.144a8 8 0 0 0-.311-.494a9.4 9.4 0 0 0-1.255-1.485C12.113 4.532 10.38 3.43 8 3.43c-2.378 0-4.112 1.101-5.238 2.182a9.4 9.4 0 0 0-1.255 1.485a8 8 0 0 0-.412.678l-.006.012l-.002.003v.001s-.001.001.414.209l-.415-.209a.47.47 0 0 0 0 .417L1.5 8l-.415.208v.002l.003.003l.006.012a3 3 0 0 0 .1.184a9.4 9.4 0 0 0 1.566 1.98c1.127 1.08 2.86 2.18 5.24 2.18c2.379 0 4.113-1.1 5.24-2.181a9.5 9.5 0 0 0 1.254-1.485a8 8 0 0 0 .391-.638l.021-.04l.006-.012l.002-.003v-.001s.001-.001-.414-.209m0 0l.415.209a.47.47 0 0 0 0-.417zM7.94 6.464a1.536 1.536 0 1 0 0 3.072a1.536 1.536 0 0 0 0-3.072M5.478 8a2.464 2.464 0 1 1 4.928 0a2.464 2.464 0 0 1-4.928 0"
            clip-rule="evenodd"
            stroke-width="0.5"
            stroke="currentColor"
        />
    </svg>
    <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
        <g fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="0.929">
            <path
                d="M8 3.895C12.447 3.895 14.5 8 14.5 8s-2.053 4.105-6.5 4.105S1.5 8 1.5 8S3.553 3.895 8 3.895Z"
            />
            <path d="M9.94 8a2 2 0 1 1-3.999 0a2 2 0 0 1 4 0Z" />
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
