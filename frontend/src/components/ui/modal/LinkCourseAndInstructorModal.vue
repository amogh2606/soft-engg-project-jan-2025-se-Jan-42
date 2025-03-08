<template>
    <Modal :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)">
        <div class="flex flex-col gap-4 py-2">
            <p class="text-xl font-semibold tracking-wide">Link Course</p>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Instructor Name</label>
                <input
                    type="text"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter instructor name"
                    v-model="instructor.name"
                    disabled
                />
            </div>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Course</label>
                <select
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    v-model="selectedCourseId"
                >
                    <option v-for="course in courses" :value="course.id">{{ course.name }}</option>
                </select>
            </div>
            <Button varient="primary" @click="linkCourse">Link Course</Button>
        </div>
    </Modal>
</template>

<script setup>
import { enrollUserInCourse } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { push } from 'notivue';
import { ref } from 'vue';
import Modal from './Modal.vue';

const props = defineProps({
    modelValue: {
        type: Boolean,
        default: false,
    },
    courses: {
        type: Array,
        default: [],
    },
    instructor: {
        type: Object,
        default: {},
    },
});
const emit = defineEmits(['update:modelValue']);

const selectedCourseId = ref(null);

const validateForm = () => {
    if (!selectedCourseId.value) {
        return false;
    }
    return true;
};

const linkCourse = () => {
    if (!validateForm()) {
        push.error('Please select a course');
        return;
    }

    enrollUserInCourse(props.instructor.id, selectedCourseId.value)
        .then((res) => {
            push.success('Course linked successfully');
            emit('update:modelValue', false);
        })
        .catch((err) => {
            console.log(err);
            push.error('Failed to link course');
        });
};
</script>
