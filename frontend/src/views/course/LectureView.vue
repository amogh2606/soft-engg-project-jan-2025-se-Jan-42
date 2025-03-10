<template>
    <div class="flex-1 overflow-y-scroll bg-gray-50">
        <div class="flex flex-col gap-4 p-4">
            <iframe
                height="315"
                :src="video?.url.replace('watch?v=', 'embed/')"
                title="YouTube video player"
                frameborder="0"
                class="w-full max-w-[560px] rounded"
            >
            </iframe>

            <div class="flex flex-col justify-center">
                <h1 class="text-2xl font-semibold">{{ video?.title }}</h1>
            </div>

            <!-- Tabs Navigation -->
            <div class="border-b border-gray-200">
                <nav class="-mb-px flex space-x-8">
                    <button
                        v-for="tab in tabs"
                        :key="tab.id"
                        @click="activeTab = tab.id"
                        :class="[
                            activeTab === tab.id
                                ? 'border-blue-500 text-blue-600'
                                : 'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700',
                            'whitespace-nowrap border-b-2 px-1 py-4 font-medium',
                        ]"
                    >
                        {{ tab.name }}
                    </button>
                </nav>
            </div>

            <!-- Tab Content -->
            <div class="mt-4 rounded-lg bg-white p-4 shadow">
                <!-- Ratings Tab -->
                <div v-if="activeTab === 'ratings'" class="flex flex-col gap-6">
                    <div class="flex items-center justify-center gap-6">
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
                        <div class="h-full w-0.5 bg-gray-300">&nbsp;</div>
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
                                <span class="ml-1 text-sm text-gray-600">
                                    ({{ video?.user_rating?.toFixed(1) || '0.0' }})
                                </span>
                            </div>
                        </div>
                    </div>
                    <Button
                        varient="secondary"
                        class="mx-auto w-auto"
                        @click="toggleRatingModal"
                        :disabled="video?.user_rating"
                        >Rate Video</Button
                    >
                </div>

                <!-- Summary Tab -->
                <div v-if="activeTab === 'summary'">
                    <div v-if="summary" class="whitespace-pre-line text-gray-700">
                        {{ summary }}
                    </div>
                    <div v-else class="flex justify-center">
                        <Button
                            varient="secondary"
                            @click="generateSummary"
                            :loading="isSummaryLoading"
                            :disabled="isSummaryLoading"
                        >
                            Generate Summary
                        </Button>
                    </div>
                </div>

                <!-- Quiz Tab -->
                <div v-if="activeTab === 'quiz'">
                    <div v-if="quiz" class="whitespace-pre-line text-gray-700">
                        {{ quiz }}
                    </div>
                    <div v-else class="flex justify-center">
                        <Button
                            varient="secondary"
                            @click="generateQuiz"
                            :loading="isQuizLoading"
                            :disabled="isQuizLoading"
                        >
                            Generate Quiz
                        </Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <SubmitVideoRatingModal
        :video-id="videoId"
        v-model="isRatingModalOpen"
        @rating-submitted="syncVideoData"
    />
</template>

<script setup>
import { generateQuizOfVideo, generateSummaryOfVideo, getVideoById } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import SubmitVideoRatingModal from '@/components/ui/modal/SubmitVideoRatingModal.vue';
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
const isSummaryLoading = ref(false);
const isQuizLoading = ref(false);
const ratingInput = ref(0);
const isRatingModalOpen = ref(false);
const activeTab = ref('ratings');
const tabs = [
    { id: 'ratings', name: 'Ratings' },
    { id: 'summary', name: 'Summary' },
    { id: 'quiz', name: 'Quiz' },
];

const toggleRatingModal = () => {
    isRatingModalOpen.value = !isRatingModalOpen.value;
};

const generateSummary = async () => {
    if (isSummaryLoading.value) return;

    // if summary is already shown, hide it
    if (showSummary.value) {
        showSummary.value = false;
        return;
    }

    // if summary is already generated, show it
    if (summary.value) {
        showSummary.value = true;
        return;
    }

    isSummaryLoading.value = true;
    generateSummaryOfVideo(props.videoId)
        .then((res) => {
            summary.value = res.data.summary;
            showSummary.value = true;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching summary !');
            showSummary.value = false;
        })
        .finally(() => {
            isSummaryLoading.value = false;
        });
};

const generateQuiz = async () => {
    if (isQuizLoading.value) return;

    // if quiz is already shown, hide it
    if (showQuiz.value) {
        showQuiz.value = false;
        return;
    }

    // if quiz is already generated, show it
    if (quiz.value) {
        showQuiz.value = true;
        return;
    }

    isQuizLoading.value = true;
    generateQuizOfVideo(props.videoId)
        .then((res) => {
            quiz.value = res.data.quiz;
            showQuiz.value = true;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching quiz !');
            showQuiz.value = false;
        })
        .finally(() => {
            isQuizLoading.value = false;
        });
};

const syncVideoData = () => {
    getVideoById(props.videoId)
        .then((res) => {
            video.value = res.data;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching video !');
        });
};

onMounted(() => {
    syncVideoData();
});
</script>
