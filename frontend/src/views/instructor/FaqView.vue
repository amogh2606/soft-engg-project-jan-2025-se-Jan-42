<script setup>
import Button from '@/components/ui/buttons/Button.vue';
import TableComponent from '@/components/ui/table/TableComponent.vue';
import { computed, onMounted, ref } from 'vue';
import BaseView from './BaseView.vue';
import { getFaqs } from '@/api';
import { push } from 'notivue';

const headers = ref([
    { label: 'Rank', key: 'rank' },
    { label: 'Question', key: 'question' },
    { label: 'Updated At', key: 'last_updated' },
]);

const faqs = ref([]);

const filteredFaqs = computed(() => {
    return faqs.value;
});

onMounted(() => {
    getFaqs()
        .then((res) => {
            faqs.value = res?.data?.faqs || [];
        })
        .catch((error) => {
            push.error(error?.response?.data?.message || 'Something went wrong fetching FAQs !');
        });
});
</script>
<template>
    <BaseView>
        <template #main-slot>
            <div class="flex flex-1 flex-col overflow-hidden pt-4">
                <div
                    class="mx-2 mb-2 flex flex-col overflow-hidden rounded-lg border bg-white p-4 shadow md:mx-10 md:mb-10"
                >
                    <h1 class="p-3 pb-7 text-center text-2xl font-semibold md:mx-10 md:px-8">
                        Frequently Asked Questions
                    </h1>

                    <div class="flex flex-col overflow-hidden rounded-lg border bg-white shadow">
                        <div class="flex justify-between gap-2 border-b p-3">
                            <input
                                type="text"
                                class="w-full rounded border p-2"
                                placeholder="Search..."
                            />
                            <Button varient="primary">Search</Button>
                        </div>

                        <TableComponent :headers="headers" :rows="filteredFaqs" />
                    </div>
                </div>
            </div>
        </template>
    </BaseView>
</template>
