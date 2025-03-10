<template>
    <Modal :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)">
        <div class="flex flex-col gap-4 py-2">
            <p class="text-xl font-semibold tracking-wide">Submit Feedback</p>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Title</label>
                <input
                    type="text"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter title"
                    v-model="title"
                />
            </div>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Description</label>
                <textarea
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter description"
                    v-model="description"
                />
            </div>
            <Button varient="primary" @click="submit">Submit</Button>
        </div>
    </Modal>
</template>

<script setup>
import { submitFeedback } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { push } from 'notivue';
import { ref, watchEffect } from 'vue';
import Modal from './Modal.vue';

const props = defineProps({
    courseId: {
        type: String,
        required: true,
    },
    modelValue: {
        type: Boolean,
        default: false,
    },
});
const emit = defineEmits(['update:modelValue']);

const title = ref('');
const description = ref('');

watchEffect(() => {
    if (props.previousRating) {
        rating.value = props.previousRating;
    }
});

const validateInput = () => {
    if (title.value === '' || description.value === '') {
        return false;
    }
    return true;
};

const submit = () => {
    if (!validateInput()) {
        push.error('Please enter valid title and description');
        return;
    }
    submitFeedback(props.courseId, title.value, description.value)
        .then((response) => {
            emit('update:modelValue', false);
            push.success('Feedback submitted successfully');
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Failed to submit feedback');
        });
};
</script>
