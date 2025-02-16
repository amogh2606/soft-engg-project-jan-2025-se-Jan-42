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
    <main class="flex h-full flex-col items-center justify-center">
        <!-- <h1 class="text-2xl font-bold">Home Page</h1>
        <p class="mt-2">This is the public home page</p> -->


        <section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-col text-center w-full mb-20">
      <h2 class="text-xs text-indigo-500 tracking-widest font-medium title-font mb-4">Indian Institute of Technology,Madras</h2>
      <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Applications Open now for May 2025 Batch | Applications Close: May 20, 2025 | Exam: July 13, 2025
    </h1>
      <p class="lg:w-2/3 mx-auto leading-relaxed text-base">IIT Madras, India's top technical institute, welcomes you to the world's first 4-year Bachelor of Science (BS) Degree in Data Science and Applications with options to exit earlier in the foundation, diploma or BSc degree level.

</p>
    </div>
    <div class="flex flex-wrap">
      <div class="xl:w-1/4 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60">
        <h2 class="text-lg sm:text-xl text-gray-900 font-medium title-font mb-2">Best Online Program</h2>
        <p class="leading-relaxed text-base mb-4">Awarded by QS Reimagine Education & The Wharton School, University of Pennsylvania</p>
        <a class="text-indigo-500 inline-flex items-center">Learn More
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
          </svg>
        </a>
      </div>
      <div class="xl:w-1/4 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60">
        <h2 class="text-lg sm:text-xl text-gray-900 font-medium title-font mb-2">Scholarship</h2>
        <p class="leading-relaxed text-base mb-4">Learners from < 5LPA eligible for up to 75% fee waivers. 2000+ students study for free</p>
        <a class="text-indigo-500 inline-flex items-center">Learn More
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
          </svg>
        </a>
      </div>
      <div class="xl:w-1/4 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60">
        <h2 class="text-lg sm:text-xl text-gray-900 font-medium title-font mb-2">No Age Limit</h2>
        <p class="leading-relaxed text-base mb-4">Learners from any age and any where in the world can study in this program. Current age of learners : 17 to 81 years.</p>
        <a class="text-indigo-500 inline-flex items-center">Learn More
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
          </svg>
        </a>
      </div>
      <div class="xl:w-1/4 lg:w-1/2 md:w-full px-8 py-6 border-l-2 border-gray-200 border-opacity-60">
        <h2 class="text-lg sm:text-xl text-gray-900 font-medium title-font mb-2">Mode of Study</h2>
        <p class="leading-relaxed text-base mb-4">Pre-recorded and synchronous sessions, Weekly Online Assignments, In-person quizzes</p>
        <a class="text-indigo-500 inline-flex items-center">Learn More
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
          </svg>
        </a>
      </div>
    </div>
    <button class="flex mx-auto mt-16 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Button</button>
  </div>
</section>
        
    </main>
</template>
