<script setup>
import { getCourseById } from '@/api';
import ChatbotDrawer from '@/components/ChatbotDrawer.vue';
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import ModulesIcon from '@/components/icons/ModulesIcon.vue';
import DraggableChatbotButton from '@/components/ui/buttons/DraggableChatbotButton.vue';
import UserDropdown from '@/components/ui/dropdown/UserDropdown.vue';
import BaseView from '@/views/BaseView.vue';
import { push } from 'notivue';
import { onMounted, ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';

const router = useRouter();
const props = defineProps({
    courseId: {
        type: String,
        required: true,
    },
});

// course_fields = {
//     'id': fields.Integer,
//     'name': fields.String,
//     'description': fields.String,
//     'videos': fields.List(fields.Nested({
//         'id': fields.Integer,
//         'title': fields.String,
//         'week': fields.Integer,
//         'lecture': fields.Integer
//     })),
//     'assignments': fields.List(fields.Nested({
//         'id': fields.Integer,
//         'week': fields.String,
//     }))
// }
const course = ref(null);
const weeklyCourseContent = ref([]);
const showWeeklyIndex = ref(true);
const drawerOpen = ref(false);
const toggleDrawer = () => {
    drawerOpen.value = !drawerOpen.value;
};

onMounted(() => {
    if (!props.courseId) {
        router.push('/404');
        return;
    }

    getCourseById(props.courseId)
        .then((res) => {
            course.value = res.data;
            // get list of weeks for which there is content like videos or assignments
            const weeks = [
                ...new Set([
                    ...new Set(res.data.videos.map((video) => video.week)),
                    ...new Set(res.data.assignments.map((assignment) => assignment.week)),
                ]),
            ].sort((a, b) => a - b);

            // create a list of weeks with videos and assignments for each week
            const content = weeks.map((week) => {
                return {
                    week,
                    content: [
                        ...res.data.videos.filter((video) => video.week === week),
                        ...res.data.assignments.filter((assignment) => assignment.week === week),
                    ],
                };
            });
            weeklyCourseContent.value = content;
            console.log(weeklyCourseContent.value);
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching course !');
        });
});
</script>
<template>
    <BaseView>
        <div class="flex h-screen w-screen flex-col">
            <header class="flex flex-wrap items-center justify-between border-b bg-white px-4 py-2">
                <RouterLink to="/">
                    <IITMLogoIcon class="me-6 h-12" />
                </RouterLink>
                <p class="me-auto rounded border bg-gray-50 p-2 font-semibold">
                    {{ course?.name || 'Course Name' }}
                </p>
                <div class="flex items-center space-x-2">
                    <UserDropdown />
                </div>
            </header>

            <div class="flex flex-1 overflow-y-hidden">
                <div class="flex h-full flex-col items-center overflow-y-scroll border-r bg-white">
                    <button
                        @click="showWeeklyIndex = !showWeeklyIndex"
                        class="flex w-full flex-col items-center justify-center bg-gray-300 p-2 transition-colors hover:bg-gray-300"
                    >
                        <ModulesIcon class="h-8 w-full" />
                        <span class="text-sm">Modules</span>
                    </button>
                </div>
                <slot
                    name="main-slot"
                    :showWeeklyIndex="showWeeklyIndex"
                    :course="course"
                    :weeklyCourseContent="weeklyCourseContent"
                />
            </div>

            <!-- Use the new draggable chatbot button component -->
            <DraggableChatbotButton :on-toggle="toggleDrawer" />
            <ChatbotDrawer :is-open="drawerOpen" :close-drawer="toggleDrawer" />
        </div>
    </BaseView>
</template>

<style scoped>
.ai-btn {
    filter: drop-shadow(2px 4px 4px black);
    transition: transform 0.2s;
}
.ai-btn:hover {
    transform: scale(1.1);
}
</style>
