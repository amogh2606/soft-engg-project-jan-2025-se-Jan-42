<script setup>
import UserIcon from '@/components/icons/UserIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import LogoutButton from '@/components/ui/buttons/LogoutButton.vue';
import { useAuthStore } from '@/stores/auth';
import { getRouteBasedOnRole } from '@/utils/routerHelper';
import { computed, onMounted, onUnmounted, ref } from 'vue';
import { RouterLink } from 'vue-router';

const props = defineProps({
    showUserName: {
        type: Boolean,
        default: true,
    },
});

// Auth state
const authStore = useAuthStore();
const user = computed(() => authStore.user);
const isLoggedIn = computed(() => authStore.isLoggedIn);

// Dashboard route based on user role
const dashboardRoute = computed(() => {
    if (!isLoggedIn.value) return '/';
    return getRouteBasedOnRole(authStore.userRole);
});

// Dropdown state
const showDropdown = ref(false);
const dropdownRef = ref(null);

const toggleDropdown = () => {
    showDropdown.value = !showDropdown.value;
};

// Close dropdown when clicking outside
const handleClickOutside = (event) => {
    if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
        showDropdown.value = false;
    }
};

onMounted(() => {
    document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
    document.removeEventListener('click', handleClickOutside);
});
</script>

<template>
    <div class="relative" ref="dropdownRef">
        <div class="flex items-center space-x-2">
            <span
                v-if="isLoggedIn && showUserName"
                class="hidden text-sm font-medium text-gray-700 md:block"
            >
                Logged in as <span class="font-bold capitalize">{{ authStore.userRole }}</span>
            </span>
            <Button varient="light" :rounded="true" @click.stop="toggleDropdown">
                <UserIcon :is-solid="false" :with-border="false" class="h-6 w-full" />
            </Button>
        </div>

        <!-- User dropdown menu -->
        <div
            v-if="showDropdown"
            class="absolute right-0 z-50 mt-2 w-48 rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
        >
            <div v-if="isLoggedIn" class="px-4 py-2 text-sm text-gray-700">
                <div class="font-medium">{{ user.name }}</div>
                <div class="truncate">{{ user.email }}</div>
            </div>
            <hr v-if="isLoggedIn" class="my-1" />

            <!-- Show dashboard link if logged in -->
            <template v-if="isLoggedIn">
                <div class="px-4 py-2">
                    <RouterLink :to="dashboardRoute" @click="showDropdown = false">
                        <Button varient="light" class="w-full">Dashboard</Button>
                    </RouterLink>
                    <hr class="my-1" />
                    <LogoutButton class="w-full" />
                </div>
            </template>
        </div>
    </div>
</template>
