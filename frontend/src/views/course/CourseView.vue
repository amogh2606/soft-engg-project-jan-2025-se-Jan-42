<script setup>
import AccordionContent from '@/components/ui/accordion/AccordionContent.vue';
import AccordionHeader from '@/components/ui/accordion/AccordionHeader.vue';
import AccordionItem from '@/components/ui/accordion/AccordionItem.vue';
import Accordion from '@/components/ui/accordion/AccordionWrapper.vue';

import { computed, ref } from 'vue';
import ActivityQuestions from './ActivityQuestions.vue';
import BaseView from './BaseView.vue';
import LectureView from './LectureView.vue';
import CourseOverview from './CourseOverview.vue';

const content = ref([
    {
        title: 'Introduction to AI',
        description: 'This is the introduction to AI',
        type: 'activity_questions',
        questions: [
            {
                question: 'What is AI?',
                options: [
                    'Artificial Intelligence',
                    'Artificial Intelligence',
                    'Artificial Intelligence',
                    'Artificial Intelligence',
                ],
                answer: 'Artificial Intelligence',
            },
            {
                question: 'What is AI?',
                options: [
                    'Artificial Intelligence',
                    'Artificial Intelligence',
                    'Artificial Intelligence',
                    'Artificial Intelligence',
                ],
                answer: 'Artificial Intelligence',
            },
        ],
    },
    {
        title: 'Introduction to AI',
        description: 'This is the introduction to AI',
        type: 'lecture',
        videoUrl: 'https://www.youtube.com/watch?v=JcI5Vnw0b2c',
    },
]);
const courseData = computed(() => {
    // create 5 weeks
    return Array.from({ length: 5 }, (_, i) => {
        return {
            title: `week ${i + 1}`,
            content: content.value,
        };
    });
});

const contentView = ref(null); // lecture or activity_questions
</script>

<template>
    <BaseView>
        <template #main-slot>
            <!-- left side for week content index -->
            <div class="flex h-full flex-col items-center overflow-y-scroll border-e">
                <Accordion :allowMultiple="false" class="!w-56">
                    <AccordionItem
                        v-for="(week, index) in courseData"
                        :key="index"
                        :id="index.toString()"
                    >
                        <AccordionHeader>
                            <div class="flex items-center gap-2">
                                <img
                                    src="../../assets/images/ring.svg"
                                    alt="ring.svg"
                                    class="h-4"
                                />
                                <p class="capitalize">{{ week.title }}</p>
                            </div>
                        </AccordionHeader>

                        <AccordionContent>
                            <div class="flex flex-col gap-2">
                                <button
                                    v-for="(item, i) in week.content"
                                    :key="i"
                                    class="flex items-center gap-2 rounded border bg-white p-2 shadow hover:bg-yellow-100"
                                    :class="contentView === item.type ? 'bg-yellow-100' : ''"
                                    @click="contentView = item.type"
                                >
                                    <img
                                        :src="
                                            item.type === 'activity_questions'
                                                ? '../../src/assets/images/clock.svg'
                                                : '../../src/assets/images/video.svg'
                                        "
                                        alt="ring.svg"
                                        class="h-4"
                                    />
                                    <p class="capitalize">{{ item.title }}</p>
                                </button>
                            </div>
                        </AccordionContent>
                    </AccordionItem>
                </Accordion>
            </div>

            <!-- right side for actual content -->
            <LectureView v-if="contentView === 'lecture'"/>
            <ActivityQuestions v-else-if="contentView === 'activity_questions'"/>
            <CourseOverview v-else/>

        </template>
    </BaseView>
</template>
