<script setup>
import IITMLogoIcon from '@/components/icons/IITMLogoIcon.vue';
import Button from '@/components/ui/buttons/Button.vue';
import { RouterLink } from 'vue-router';
</script>
<template>
    <header class="flex flex-wrap items-center justify-between border-b bg-white px-4 py-2">
        <RouterLink to="/">
            <IITMLogoIcon class="h-12" />
        </RouterLink>
        <div class="flex space-x-2">
            <RouterLink to="/auth/login">
                <Button varient="primary">Login</Button>
            </RouterLink>
            <RouterLink to="/auth/signup">
                <Button varient="primary">Signup</Button>
            </RouterLink>
        </div>
    </header>
    <main class="flex h-full flex-col overflow-y-scroll">
        <section class="body-font text-gray-600">
            <div class="container mx-auto px-5 py-8">
                <div class="mb-8 flex w-full flex-col text-center bg-white rounded-lg shadow p-8">
                    <h1 class="text-2xl mb-4 font-medium tracking-widest text-indigo-500">
                        Indian Institute of Technology,Madras
                    </h1>
                    <p class="mx-auto text-base leading-relaxed lg:w-2/3">
                        IIT Madras, India's top technical institute, welcomes you to the world's
                        first 4-year Bachelor of Science (BS) Degree in Data Science and
                        Applications with options to exit earlier in the foundation, diploma or BSc
                        degree level.
                    </p>
                </div>
                <div class="flex flex-wrap bg-white rounded-lg shadow py-8 !mb-8">
                    <div
                        class="border-l-2 border-gray-200 border-opacity-60 px-8 py-6 md:w-full lg:w-1/2 xl:w-1/4"
                    >
                        <h2 class="title-font mb-2 text-lg font-medium text-gray-900 sm:text-xl">
                            Best Online Program
                        </h2>
                        <p class="mb-4 text-base leading-relaxed">
                            Awarded by QS Reimagine Education & The Wharton School, University of
                            Pennsylvania
                        </p>
                    </div>
                    <div
                        class="border-l-2 border-gray-200 border-opacity-60 px-8 py-6 md:w-full lg:w-1/2 xl:w-1/4"
                    >
                        <h2 class="title-font mb-2 text-lg font-medium text-gray-900 sm:text-xl">
                            Scholarship
                        </h2>
                        <p class="mb-4 text-base leading-relaxed">
                            Learners from < 5LPA eligible for up to 75% fee waivers. 2000+ students
                            study for free
                        </p>
                    </div>
                    <div
                        class="border-l-2 border-gray-200 border-opacity-60 px-8 py-6 md:w-full lg:w-1/2 xl:w-1/4"
                    >
                        <h2 class="title-font mb-2 text-lg font-medium text-gray-900 sm:text-xl">
                            No Age Limit
                        </h2>
                        <p class="mb-4 text-base leading-relaxed">
                            Learners from any age and any where in the world can study in this
                            program. Current age of learners : 17 to 81 years.
                        </p>
                    </div>
                    <div
                        class="border-l-2 border-gray-200 border-opacity-60 px-8 py-6 md:w-full lg:w-1/2 xl:w-1/4"
                    >
                        <h2 class="title-font mb-2 text-lg font-medium text-gray-900 sm:text-xl">
                            Mode of Study
                        </h2>
                        <p class="mb-4 text-base leading-relaxed">
                            Pre-recorded and synchronous sessions, Weekly Online Assignments,
                            In-person quizzes
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>
