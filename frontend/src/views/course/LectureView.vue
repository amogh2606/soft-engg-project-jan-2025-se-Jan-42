<template>
    <div class="flex-1 overflow-y-scroll bg-gray-50">
        <div class="flex flex-col gap-4 p-4">
            <div class="flex flex-col justify-center">
                <h1 class="text-2xl font-semibold">{{ video?.title }}</h1>
                <div class="mt-2 flex items-center gap-6">
                    <div class="flex items-center">
                        <span class="mr-2 text-sm text-gray-600">Average Rating:</span>
                        <div class="flex">
                            <template v-for="i in 5" :key="`avg-${i}`">
                                <svg
                                    class="h-5 w-5"
                                    :class="
                                        i <= (video?.avg_rating || 0)
                                            ? 'text-yellow-400'
                                            : 'text-gray-300'
                                    "
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24"
                                    fill="currentColor"
                                >
                                    <path
                                        d="M12 1.5l3.09 6.83 7.91.95-5.82 5.23 1.42 7.99L12 18.75l-6.6 3.75 1.42-7.99L1 9.28l7.91-.95L12 1.5z"
                                    />
                                </svg>
                            </template>
                            <span class="ml-1 text-sm text-gray-600">
                                ({{ video?.avg_rating?.toFixed(1) || '0.0' }})
                            </span>
                        </div>
                    </div>
                    <div class="flex items-center">
                        <span class="mr-2 text-sm text-gray-600">Your Rating:</span>
                        <div class="flex">
                            <template v-for="i in 5" :key="`user-${i}`">
                                <svg
                                    class="h-5 w-5"
                                    :class="
                                        i <= (video?.user_rating || 0)
                                            ? 'text-yellow-400'
                                            : 'text-gray-300'
                                    "
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24"
                                    fill="currentColor"
                                >
                                    <path
                                        d="M12 1.5l3.09 6.83 7.91.95-5.82 5.23 1.42 7.99L12 18.75l-6.6 3.75 1.42-7.99L1 9.28l7.91-.95L12 1.5z"
                                    />
                                </svg>
                            </template>
                        </div>
                    </div>
                </div>
            </div>

            <iframe
                height="315"
                :src="video?.url.replace('watch?v=', 'embed/')"
                title="YouTube video player"
                frameborder="0"
                class="mx-auto w-full max-w-[560px] rounded"
            >
            </iframe>

            <div class="mt-4 flex justify-center gap-4">
                <Button
                    :varient="showSummary ? 'secondary' : 'light'"
                    @click="toggleSummary"
                    :disabled="isSummaryLoading"
                    :loading="isSummaryLoading"
                >
                    {{ showSummary ? 'Hide Summary' : 'Show Summary' }}
                </Button>
                <Button
                    :varient="showQuiz ? 'secondary' : 'light'"
                    @click="toggleQuiz"
                    :disabled="isQuizLoading"
                    :loading="isQuizLoading"
                >
                    {{ showQuiz ? 'Hide Quiz' : 'Show Quiz' }}
                </Button>
            </div>

            <!-- Summary Section -->
            <div v-if="showSummary" class="mt-4 rounded-lg bg-white p-4 shadow">
                <h2 class="mb-2 text-xl font-semibold">Video Summary</h2>
                <p class="whitespace-pre-line text-gray-700">{{ summary }}</p>
            </div>

            <!-- Quiz Section -->
            <div v-if="showQuiz" class="mt-4 rounded-lg bg-white p-4 shadow">
                <h2 class="mb-4 text-xl font-semibold">Quiz</h2>
                <p class="whitespace-pre-line text-gray-700">{{ quiz }}</p>
            </div>
        </div>
    </div>
    <LoadingOverlay :show="isSummaryLoading || isQuizLoading" message="Loading..." />
</template>

<script setup>
import { generateQuizOfVideo, generateSummaryOfVideo, getVideoById } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import LoadingOverlay from '@/components/ui/overlays/LoadingOverlay.vue';
import { push } from 'notivue';
import { onMounted, ref } from 'vue';

// https://www.youtube.com/embed/lEMtlAqlJww
const props = defineProps({
    videoId: {
        type: String,
        required: true,
    },
});

const video = ref(null);
const showSummary = ref(false);
const showQuiz = ref(false);
const summary = ref(null);
const quiz = ref(null);
const userAnswers = ref([]);
const isSummaryLoading = ref(false);
const isQuizLoading = ref(false);

const generateSummary = async () => {
    if (isSummaryLoading.value) return;
    if (summary.value) return;

    isSummaryLoading.value = true;
    generateSummaryOfVideo(props.videoId)
        .then((res) => {
            summary.value = res.data.summary;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching summary !');
        })
        .finally(() => {
            isSummaryLoading.value = false;
        });
};

const generateQuiz = async () => {
    if (isQuizLoading.value) return;
    if (quiz.value) return;
    
    isQuizLoading.value = true;
    generateQuizOfVideo(props.videoId)
        .then((res) => {
            quiz.value = res.data.quiz;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching quiz !');
        })
        .finally(() => {
            isQuizLoading.value = false;
        });
};

const toggleSummary = () => {
    showSummary.value = !showSummary.value;
    if (showSummary.value) {
        generateSummary();
    }
};

const toggleQuiz = () => {
    showQuiz.value = !showQuiz.value;
    if (showQuiz.value) {
        generateQuiz();
    }
};

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
