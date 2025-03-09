<template>
    <div class="flex-1 overflow-y-scroll bg-gray-50">
        <div class="flex flex-col gap-4 p-4 md:px-8">
            <div class="flex flex-col justify-center">
                <h1 class="text-2xl font-semibold">Activity Questions</h1>
                <p class="text-gray-500">General Instructions Here ...</p>
            </div>
            <div class="flex flex-col gap-4">
                <div
                    class="flex flex-col gap-2 rounded bg-white p-4 shadow"
                    v-for="question in assignment?.questions"
                    :key="question.id"
                >
                    <p class="font-semibold">
                        <span>{{ question.qno }}) {{ question.text }}</span>
                    </p>
                    <div class="flex flex-col gap-2">
                        <label
                            v-for="optionNum in 4"
                            :key="optionNum"
                            class="flex items-center gap-2"
                            :class="{
                                'text-green-600':
                                    isSubmitted &&
                                    question[`option_${optionNum}`] ===
                                        question[`option_${question.correct_option}`],
                                'text-red-600':
                                    isSubmitted &&
                                    selectedAnswers[question.id] ===
                                        question[`option_${optionNum}`] &&
                                    question[`option_${optionNum}`] !==
                                        question[`option_${question.correct_option}`],
                            }"
                        >
                            <input
                                type="radio"
                                :name="`question${question.id}`"
                                :value="question[`option_${optionNum}`]"
                                v-model="selectedAnswers[question.id]"
                                :disabled="isSubmitted"
                            />
                            <span>{{ question[`option_${optionNum}`] }}</span>
                        </label>
                    </div>
                    <div class="flex justify-end">
                        <Button
                            varient="light"
                            :rounded="true"
                            @click="handleQuestionHelp(question.id)"
                        >
                            <HelpIcon class="h-4 w-4" />
                        </Button>
                    </div>
                </div>
            </div>
            <div class="flex justify-start gap-4">
                <Button @click="handleSubmit" varient="secondary" :disabled="isSubmitted"
                    >Submit</Button
                >
                <Button v-if="isSubmitted" @click="handleRetry" varient="secondary"
                    >Try Again</Button
                >
            </div>
        </div>
    </div>
</template>

<script setup>
import { createChatbotSessionForQuestionHelp, getAssignmentById } from '@/api';
import HelpIcon from '@/components/icons/HelpIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import { push } from 'notivue';
import { onMounted, reactive, ref } from 'vue';

const props = defineProps({
    assignmentId: {
        type: String,
        required: true,
    },
    courseId: {
        type: Number,
        required: true,
    },
});

const assignment = ref(null);
const selectedAnswers = reactive({});
const isSubmitted = ref(false);

const handleSubmit = () => {
    isSubmitted.value = true;
};

const handleRetry = () => {
    isSubmitted.value = false;
    Object.keys(selectedAnswers).forEach((key) => {
        delete selectedAnswers[key];
    });
};

onMounted(() => {
    getAssignmentById(props.assignmentId)
        .then((res) => {
            assignment.value = res.data;
        })
        .catch((error) => {
            push.error(
                error?.response?.data?.message || 'Something went wrong fetching assignment !',
            );
        });
});

const handleQuestionHelp = (questionId) => {
    createChatbotSessionForQuestionHelp(props.courseId, props.assignmentId, questionId)
        .then((res) => {
            push.info('Chatbot session created for question help');
        })
        .catch((error) => {
            push.error(
                error?.response?.data?.message ||
                    'Something went wrong creating chatbot session for question help',
            );
        });
};
</script>
