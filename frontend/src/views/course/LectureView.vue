<template>
    <div class="flex-1 overflow-y-scroll bg-gray-50">
        <div class="flex flex-col gap-4 p-4">
            <div class="flex flex-col justify-center">
                <h1 class="text-2xl font-semibold">{{ video?.title }}</h1>
                <p class="text-gray-500">This is the introduction to AI</p>
            </div>
            <iframe
                height="315"
                :src="video?.url.replace('watch?v=', 'embed/')"
                title="YouTube video player"
                frameborder="0"
                class="mx-auto w-full max-w-[560px] rounded"
            >
            </iframe>
        </div>
    </div>
</template>

<script setup>
import { getVideoById } from '@/api';
import { push } from 'notivue';
import { onMounted, ref } from 'vue';

// https://www.youtube.com/embed/lEMtlAqlJww
const props = defineProps({
    videoId: {
        type: String,
        required: true,
    },
});

// {
//     'id': video.id,
//     'course_id': video.course_id,
//     'week': video.week,
//     'lecture': video.lecture,
//     'title': video.title,
//     'url': video.url,    https://www.youtube.com/watch?v=81BaOIrfvJA
//     'avg_rating': video.avg_rating,
//     'user_rating': user_rating
// }
const video = ref(null);

onMounted(() => {
    getVideoById(props.videoId)
        .then((res) => {
            video.value = res.data;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching video !');
        });
});
</script>
