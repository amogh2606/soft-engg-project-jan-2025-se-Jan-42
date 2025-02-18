<template>
    <Modal :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)">
        <div class="flex flex-col gap-4 p-4">
            <p class="text-xl font-semibold tracking-wide">Upload File</p>

            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">File Name</label>
                <input
                    type="text"
                    class="rounded-md border p-2 text-gray-600 focus:outline-none focus:ring-1 focus:ring-gray-300"
                    placeholder="Enter file name"
                />
            </div>

            <div class="flex flex-col gap-2">
                <label class="text-sm font-medium text-gray-600">Select File</label>
                <input
                    type="file"
                    @change="handleFileUpload"
                    class="rounded-md border p-2"
                    ref="fileInputRef"
                />
            </div>

            <div
                v-if="fileName"
                class="flex flex-wrap items-center justify-between gap-2 rounded-md bg-gray-100 p-2"
            >
                <span class="text-sm text-gray-700">{{ fileName }}</span>
                <button @click="removeFile" class="text-sm font-medium text-red-500">Remove</button>
            </div>

            <button
                @click="uploadFile"
                class="rounded-md bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
            >
                Upload
            </button>
        </div>
    </Modal>
</template>

<script setup>
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
const fileName = ref(null);
const fileInputRef = ref(null);

const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
        fileName.value = file.name;
    } else {
        fileName.value = null;
    }
};

const removeFile = () => {
    fileName.value = null;
    fileInputRef.value.value = null;
};

const uploadFile = () => {
    if (!fileName.value) {
        push.error({
            title: 'Error',
            message: 'Please select a file to upload.',
        });
        return;
    }
    push.success({
        title: 'File uploaded',
        message: `File ${fileName.value} uploaded successfully`,
    });

    emit('update:modelValue', false);
    fileName.value = null;
    fileInputRef.value.value = null;
};
</script>
