<template>
    <div class="flex-1 overflow-y-scroll bg-gray-50">
        <div class="flex flex-col gap-4 p-4">
            <div class="flex flex-col justify-center">
                <h1 class="text-2xl font-semibold">Lecture Title</h1>
                <p class="text-gray-500">This is the introduction to AI</p>
            </div>
            <iframe
                height="315"
                src="https://www.youtube.com/embed/lEMtlAqlJww"
                title="YouTube video player"
                frameborder="0"
                class="rounded w-full max-w-[560px]"
            >
            </iframe>
            <div class="flex flex-wrap gap-4">
                <button class="rounded border border-black bg-white px-8 py-2 hover:bg-gray-600">
                    <img src="../../assets/images/ai.png" alt="ai" class="h-6" />
                </button>
                <button class="rounded border border-black bg-white px-8 py-2 hover:bg-gray-600">
                    <img src="../../assets/images/ai.png" alt="ai" class="h-6" />
                </button>
                <button class="rounded border border-black bg-white px-8 py-2 hover:bg-gray-600">
                    <img src="../../assets/images/ai.png" alt="ai" class="h-6" />
                </button>
            </div>
        </div>
    </div>
</template>
