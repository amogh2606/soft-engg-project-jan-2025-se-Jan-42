<template>
    <div class="flex-1 overflow-y-scroll bg-gray-50">
        <div class="flex flex-col gap-4 p-4">
            <div class="flex flex-col justify-center">
                <h1 class="text-2xl font-semibold">Activity Questions</h1>
                <p class="text-gray-500">General Instructions Here ...</p>
            </div>
            <div class="flex flex-col gap-4">
                <div class="flex flex-col gap-2 rounded bg-white p-4 shadow">
                    <p class="text-lg font-semibold">
                        <span>1) What is 2 + 2 ?</span>
                    </p>
                    <div class="flex flex-col gap-2">
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 4</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 5</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 6</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 7</span>
                        </label>
                    </div>
                </div>
                <div class="flex flex-col gap-2 rounded bg-white p-4 shadow">
                    <p class="text-lg font-semibold">
                        <span>2) What is 2 + 2 ?</span>
                    </p>
                    <div class="flex flex-col gap-2">
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 4</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 5</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 6</span>
                        </label>
                        <label class="flex items-center gap-2">
                            <input type="radio" name="question1" />
                            <span>The answer is : 7</span>
                        </label>
                    </div>
                </div>
            </div>
            <div class="flex justify-start">
                <button class="rounded bg-black px-8 py-2 text-white hover:opacity-80">
                    Submit
                </button>
            </div>
        </div>
    </div>
</template>
