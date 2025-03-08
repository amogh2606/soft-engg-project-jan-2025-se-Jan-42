<script setup>
import AccordionContent from '@/components/ui/accordion/AccordionContent.vue';
import AccordionHeader from '@/components/ui/accordion/AccordionHeader.vue';
import AccordionItem from '@/components/ui/accordion/AccordionItem.vue';
import Accordion from '@/components/ui/accordion/AccordionWrapper.vue';

import ClockIcon from '@/components/icons/ClockIcon.vue';
import RingIcon from '@/components/icons/RingIcon.vue';
import VideoIcon from '@/components/icons/VideoIcon.vue';
import { ref } from 'vue';
import ActivityQuestions from './ActivityQuestions.vue';
import BaseView from './BaseView.vue';
import CourseOverview from './CourseOverview.vue';
import LectureView from './LectureView.vue';

const contentView = ref(null); // lecture or activity_questions
const selectedAccordionItem = ref(null);
const handleAccordionItemClick = (item, uniqueId) => {
    contentView.value = item.lecture ? 'lecture' : 'activity_questions';
    selectedAccordionItem.value = uniqueId;
};
</script>

<template>
    <BaseView>
        <template v-slot:main-slot="{ showWeeklyIndex, course, weeklyCourseContent }">
            <!-- left side for week content index -->
            <div
                class="flex h-full flex-col items-center overflow-y-scroll border-r bg-white"
                v-show="showWeeklyIndex"
            >
                <!-- About Course Button -->
                <button
                    class="flex w-full items-center gap-2 border-b border-gray-200 px-6 py-4 hover:bg-yellow-50"
                    :class="contentView === null ? 'bg-yellow-50' : ''"
                    @click="
                        contentView = null;
                        selectedAccordionItem = null;
                    "
                >
                    <RingIcon class="h-4 w-4" />
                    <p class="capitalize">About Course</p>
                </button>

                <Accordion :allowMultiple="false" class="!w-64">
                    <AccordionItem
                        v-for="(week, index) in weeklyCourseContent"
                        :key="index"
                        :id="index.toString()"
                    >
                        <AccordionHeader>
                            <div class="flex items-center gap-2">
                                <RingIcon class="h-4 w-4" />
                                <p class="capitalize">Week {{ week.week }}</p>
                            </div>
                        </AccordionHeader>

                        <AccordionContent>
                            <div class="flex flex-col gap-2">
                                <button
                                    v-for="(item, i) in week.content"
                                    :key="i"
                                    class="flex items-center gap-3 rounded border bg-white p-2 text-gray-700 shadow hover:bg-yellow-50"
                                    :class="
                                        selectedAccordionItem ===
                                        week.week.toString() + '-' + i + '-' + item.id
                                            ? 'bg-yellow-50'
                                            : ''
                                    "
                                    @click="
                                        handleAccordionItemClick(
                                            item,
                                            week.week.toString() + '-' + i + '-' + item.id,
                                        )
                                    "
                                >
                                    <component
                                        :is="item.lecture ? VideoIcon : ClockIcon"
                                        class="h-4 w-4 shrink-0"
                                    />
                                    <div class="h-full w-0.5 bg-gray-300">&nbsp;</div>
                                    <p class="text-start text-sm capitalize">
                                        {{ item.lecture ? item.title : `Assignment ${item.id}` }}
                                    </p>
                                </button>
                            </div>
                        </AccordionContent>
                    </AccordionItem>
                </Accordion>
            </div>

            <!-- right side for actual content -->
            <LectureView
                v-if="contentView === 'lecture'"
                :key="'lv' + selectedAccordionItem"
                :videoId="selectedAccordionItem.split('-')[2]"
            />
            <ActivityQuestions
                v-else-if="contentView === 'activity_questions'"
                :key="'aq' + selectedAccordionItem"
                :assignmentId="selectedAccordionItem.split('-')[2]"
            />
            <CourseOverview v-else :course="course" />
        </template>
    </BaseView>
</template>
