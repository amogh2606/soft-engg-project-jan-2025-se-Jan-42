<script setup>
import ChatbotIcon from '@/components/icons/ChatbotIcon.vue';
import { onBeforeUnmount, onMounted, ref } from 'vue';

// Props
const props = defineProps({
    onToggle: {
        type: Function,
        required: true,
    },
});

// Position tracking for draggable button
const buttonPosition = ref({ x: null, y: null });
const isDragging = ref(false);
const dragOffset = ref({ x: 0, y: 0 });
// Flag to track if any movement occurred during dragging
const hasMoved = ref(false);

// Functions to save and load position from local storage
const savePosition = () => {
    localStorage.setItem('chatbotButtonPosition', JSON.stringify(buttonPosition.value));
};

const loadPosition = () => {
    const savedPosition = localStorage.getItem('chatbotButtonPosition');
    return savedPosition ? JSON.parse(savedPosition) : null;
};

// Initialize default position
onMounted(() => {
    // Try to load position from local storage first
    const savedPosition = loadPosition();

    // Use saved position or default to bottom-right
    if (savedPosition) {
        buttonPosition.value = savedPosition;
    } else {
        buttonPosition.value = { x: window.innerWidth - 100, y: window.innerHeight - 100 };
    }

    // Add window resize listener to ensure button stays within viewport
    window.addEventListener('resize', updateButtonPosition);
});

onBeforeUnmount(() => {
    window.removeEventListener('resize', updateButtonPosition);
});

const updateButtonPosition = () => {
    if (buttonPosition.value.x > window.innerWidth - 50) {
        buttonPosition.value.x = window.innerWidth - 50;
    }
    if (buttonPosition.value.y > window.innerHeight - 50) {
        buttonPosition.value.y = window.innerHeight - 50;
    }
    savePosition(); // Save position after adjustments
};

const startDrag = (event) => {
    isDragging.value = true;
    hasMoved.value = false; // Reset movement flag
    dragOffset.value = {
        x: event.clientX - buttonPosition.value.x,
        y: event.clientY - buttonPosition.value.y,
    };

    // Add global mouse move and up listeners
    document.addEventListener('mousemove', onDrag);
    document.addEventListener('mouseup', stopDrag);

    // Prevent default to avoid text selection during drag
    event.preventDefault();
};

const onDrag = (event) => {
    if (isDragging.value) {
        // Calculate new position with constraints
        const newX = Math.max(
            0,
            Math.min(window.innerWidth - 60, event.clientX - dragOffset.value.x),
        );
        const newY = Math.max(
            0,
            Math.min(window.innerHeight - 60, event.clientY - dragOffset.value.y),
        );

        // Set hasMoved flag if position changed
        if (newX !== buttonPosition.value.x || newY !== buttonPosition.value.y) {
            hasMoved.value = true;
        }

        buttonPosition.value = { x: newX, y: newY };
    }
};

const stopDrag = () => {
    isDragging.value = false;
    document.removeEventListener('mousemove', onDrag);
    document.removeEventListener('mouseup', stopDrag);

    // Save position to local storage when drag ends
    if (hasMoved.value) {
        savePosition();
    }
};

// Handle click separately from drag
const handleButtonClick = () => {
    if (!hasMoved.value) {
        props.onToggle();
    }
};
</script>

<template>
    <button
        class="ai-btn fixed select-none transition-transform"
        @mousedown="startDrag"
        @click="handleButtonClick"
        :style="{
            left: `${buttonPosition.x}px`,
            top: `${buttonPosition.y}px`,
        }"
    >
        <ChatbotIcon class="h-12 w-auto" />
    </button>
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
