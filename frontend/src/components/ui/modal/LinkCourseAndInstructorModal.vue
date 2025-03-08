<template>
    <Modal :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)">
        <div class="flex flex-col gap-4 py-2">
            <p class="text-xl font-semibold tracking-wide">Add Instructor</p>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Name</label>
                <input
                    type="text"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter instructor name"
                    v-model="name"
                />
            </div>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Email</label>
                <input
                    type="email"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter instructor email"
                    v-model="email"
                />
            </div>
            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Password</label>
                <input
                    type="password"
                    class="rounded-md border border-gray-400 p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-400"
                    placeholder="Enter instructor password"
                    v-model="password"
                />
            </div>
            <Button varient="primary" @click="addInstructor">Add Instructor</Button>
        </div>
    </Modal>
</template>

<script setup>
import { registerUser } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { push } from 'notivue';
import { ref } from 'vue';
import Modal from './Modal.vue';

defineProps({
    modelValue: {
        type: Boolean,
        default: false,
    },
});
const emit = defineEmits(['update:modelValue']);

const name = ref('');
const email = ref('');
const password = ref('');

const validateForm = () => {
    if (!name.value || !email.value || !password.value) {
        return false;
    }
    return true;
};

const addInstructor = () => {
    if (!validateForm()) {
        push.error('Please fill all fields !');
        return;
    }

    registerUser(name.value, email.value, password.value)
        .then((res) => {
            console.log('addInstructor', res);
            emit('update:modelValue', false);
            push.success('Instructor added successfully');
        })
        .catch((err) => {
            if (err?.response?.status === 400) {
                push.error(err?.response?.data?.message || 'Failed to add instructor');
            } else {
                push.error('Failed to add instructor');
            }
        });
};
</script>
