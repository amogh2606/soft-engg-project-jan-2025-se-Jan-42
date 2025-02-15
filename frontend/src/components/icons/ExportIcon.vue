<template>
    <svg
        v-if="isSolid"
        xmlns="http://www.w3.org/2000/svg"
        version="1.1"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        width="512"
        height="512"
        x="0"
        y="0"
        viewBox="0 0 24 24"
        style="enable-background: new 0 0 512 512"
        xml:space="preserve"
    >
        <g>
            <path
                d="M21 13a1 1 0 0 0-1 1v3a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3h5a1 1 0 0 0 0-2H7a5.006 5.006 0 0 0-5 5v10a5.006 5.006 0 0 0 5 5h10a5.006 5.006 0 0 0 5-5v-3a1 1 0 0 0-1-1z"
                fill="currentColor"
                opacity="1"
                data-original="#000000"
            ></path>
            <path
                d="M7.01 13.142a1 1 0 0 0 .83.845A.968.968 0 0 0 8 14a1 1 0 0 0 .895-.553c1.241-2.483 4.543-2.632 6.105-2.539V13a1 1 0 0 0 1.707.707l5-5a1 1 0 0 0-.082-1.488l-5-4A1 1 0 0 0 15 4v1.918c-2.8-.131-4.94.535-6.341 1.979a6.725 6.725 0 0 0-1.649 5.245z"
                fill="currentColor"
                opacity="1"
                data-original="#000000"
            ></path>
        </g>
    </svg>
    <svg
        v-else
        xmlns="http://www.w3.org/2000/svg"
        version="1.1"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        width="512"
        height="512"
        x="0"
        y="0"
        viewBox="0 0 24 24"
        style="enable-background: new 0 0 512 512"
        xml:space="preserve"
    >
        <g>
            <path
                d="M21 13a1 1 0 0 0-1 1v3a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3h5a1 1 0 0 0 0-2H7a5.006 5.006 0 0 0-5 5v10a5.006 5.006 0 0 0 5 5h10a5.006 5.006 0 0 0 5-5v-3a1 1 0 0 0-1-1z"
                fill="currentColor"
                opacity="1"
                data-original="#000000"
            ></path>
            <path
                d="M7.01 13.142a1 1 0 0 0 .83.845A.968.968 0 0 0 8 14a1 1 0 0 0 .895-.553c1.241-2.483 4.543-2.632 6.105-2.539V13a1 1 0 0 0 1.707.707l5-5a1 1 0 0 0-.082-1.488l-5-4A1 1 0 0 0 15 4v1.918c-2.8-.131-4.94.535-6.341 1.979a6.725 6.725 0 0 0-1.649 5.245zM10.1 9.29c1.127-1.162 3.076-1.6 5.8-1.3a1.018 1.018 0 0 0 .777-.249A1 1 0 0 0 17 7v-.919l2.5 2-2.5 2.5V10a1 1 0 0 0-.835-.986 11.758 11.758 0 0 0-1.807-.128 9.959 9.959 0 0 0-4.785 1.1 3.567 3.567 0 0 1 .527-.696z"
                fill="currentColor"
                opacity="1"
                data-original="#000000"
            ></path>
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
