<template>
    <div class="flex-1 overflow-y-scroll bg-gray-50">
        <div class="flex flex-col gap-4 p-4 md:px-8">
            <div class="flex flex-col justify-center">
                <h1 class="text-2xl font-semibold">Activity Questions</h1>
                <p class="text-gray-500">General Instructions Here ...</p>
            </div>
            <div class="flex flex-col gap-4">
                <div class="flex flex-col gap-2 rounded bg-white p-4 shadow" v-for="question in assignment?.questions" :key="question.id">
                    <p class="font-semibold">
                        <span>{{ question.qno }}) {{ question.text }}</span>
                    </p>
                    <div class="flex flex-col gap-2">
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" :value="question.option_1" />
                            <span>{{ question.option_1 }}</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" :value="question.option_2" />
                            <span>{{ question.option_2 }}</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" :value="question.option_3" />
                            <span>{{ question.option_3 }}</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" :value="question.option_4" />
                            <span>{{ question.option_4 }}</span>
                        </label>
                    </div>
                </div>
            </div>
            <div class="flex justify-start">
                <Button varient="secondary">Submit</Button>
            </div>
        </div>
    </div>
</template>

<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import { getAssignmentById } from '@/api';
import { onMounted, ref } from 'vue';
import { push } from 'notivue';

const props = defineProps({
    assignmentId: {
        type: String,
        required: true,
    },
});

// question_fields = {
//     'id': fields.Integer,
//     'qno': fields.Integer,
//     'type': fields.String,
//     'text': fields.String,
//     'option_1': fields.String,
//     'option_2': fields.String,
//     'option_3': fields.String,
//     'option_4': fields.String,
//     'correct_option': fields.Integer
// }

// assignment_fields = {
//     'id': fields.Integer,
//     'course_id': fields.Integer,
//     'week': fields.Integer,
//     'due_date': fields.String,
//     'questions': fields.List(fields.Nested(question_fields))
// }

const assignment = ref(null);

onMounted(() => {
    getAssignmentById(props.assignmentId)
        .then((res) => {
            assignment.value = res.data;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching assignment !');
        });
});
</script>
