<template>
    <Modal :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)">
        <div class="flex flex-col gap-4 py-2">
            <p class="text-xl font-semibold tracking-wide">Update Course</p>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Name</label>
                <input
                    type="text"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter course name"
                    v-model="name"
                />
            </div>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Description</label>
                <input
                    type="text"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter course description"
                    v-model="description"
                />
            </div>
            <Button varient="primary" @click="submit">Update Course</Button>
        </div>
    </Modal>
</template>

<script setup>
import { updateCourse } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { push } from 'notivue';
import { ref, watchEffect } from 'vue';
import Modal from './Modal.vue';

const props = defineProps({
    course: {
        type: Object,
        required: true,
    },
    modelValue: {
        type: Boolean,
        default: false,
    },
});
const emit = defineEmits(['update:modelValue']);

const name = ref(props.course?.name || '');
const description = ref(props.course?.description || '');

watchEffect(() => {
    name.value = props.course?.name || '';
    description.value = props.course?.description || '';
});

const validateInput = () => {
    if (name.value.length === 0 || description.value.length === 0) {
        return false;
    }
    return true;
};

const submit = () => {
    if (!validateInput()) {
        push.error('Please fill all fields');
        return;
    }
    updateCourse(props.course.id, name.value, description.value)
        .then((response) => {
            emit('update:modelValue', false);
            push.success('Course updated successfully');
        })
        .catch((error) => {
            if (error.response.status === 400) {
                push.error('Course already exists');
            } else {
                push.error('Failed to update course');
            }
        });
};
</script>
