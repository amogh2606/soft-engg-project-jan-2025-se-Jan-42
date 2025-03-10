<template>
    <Modal :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)">
        <div class="flex flex-col gap-4 py-2">
            <p class="text-xl font-semibold tracking-wide">Rate Video</p>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Rating</label>
                <input
                    type="number"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter rating (1-5)"
                    :min="1"
                    :max="5"
                    :step="0.5"
                    v-model="rating"
                />
            </div>
            <Button varient="primary" @click="submit">Submit</Button>
        </div>
    </Modal>
</template>

<script setup>
import { giveRatingToVideo } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { push } from 'notivue';
import { ref, watchEffect } from 'vue';
import Modal from './Modal.vue';

const props = defineProps({
    videoId: {
        type: String,
        required: true,
    },
    previousRating: {
        type: Number,
        default: 0,
    },
    modelValue: {
        type: Boolean,
        default: false,
    },
});
const emit = defineEmits(['update:modelValue']);

const rating = ref(0);

watchEffect(() => {
    if (props.previousRating) {
        rating.value = props.previousRating;
    }
});

const validateInput = () => {
    if (rating.value === 0) {
        return false;
    }
    return true;
};

const submit = () => {
    if (!validateInput()) {
        push.error('Please enter a rating between 1 and 5');
        return;
    }
    giveRatingToVideo(props.videoId, rating.value)
        .then((response) => {
            emit('update:modelValue', false);
            push.success('Rating given successfully');
            emit('rating-submitted');
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Failed to give rating');
        });
};
</script>
