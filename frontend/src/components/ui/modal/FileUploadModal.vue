<template>
    <Modal :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)">
        <div class="flex flex-col gap-4 p-4">
            <p class="text-xl font-semibold tracking-wide">Upload File</p>

            <div class="flex flex-col gap-2">
                <label class="hidden text-sm font-medium text-gray-600">Select File</label>
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

            <Button @click="uploadFile" :loading="isLoading">
                <span>Upload</span>
            </Button>
        </div>
    </Modal>
</template>

<script setup>
import { uploadDocumentToKnowledgeStack } from '@/api';
import Button from '@/components/ui/buttons/Button.vue';
import { push } from 'notivue';
import { ref } from 'vue';
import Modal from './Modal.vue';
const props = defineProps({
    modelValue: {
        type: Boolean,
        default: false,
    },
    courseId: {
        type: String,
        required: true,
    },
});

const emit = defineEmits(['update:modelValue']);
const fileName = ref(null);
const fileInputRef = ref(null);
const isLoading = ref(false);

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

const validateInput = () => {
    if (!fileName.value || !fileInputRef.value.files[0]) {
        return false;
    }
    return true;
};

const uploadFile = () => {
    if (!validateInput()) {
        push.error({
            title: 'Error',
            message: 'Please select a file to upload.',
        });
        return;
    }

    isLoading.value = true;
    const formData = new FormData();
    formData.append('file', fileInputRef.value.files[0]);

    uploadDocumentToKnowledgeStack(props.courseId, formData)
        .then((response) => {
            push.success({
                title: 'File uploaded',
                message: `File ${fileName.value} uploaded successfully`,
            });

            emit('update:modelValue', false);
            fileName.value = null;
            fileInputRef.value.value = null;
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Failed to upload file !');
        })
        .finally(() => {
            isLoading.value = false;
        });
};
</script>
