<script setup lang="ts">
import {Toggle} from "~/components/ui/toggle";

const model = defineModel<boolean>();
const props = defineProps<{ name: string }>();
</script>

<template>
    <Toggle v-model:pressed="model" variant="outline" class="w-36 h-36 flex flex-col" :class="[model ? 'border-primary' : '']">
        <slot />
        <p class="mb-4 font-bold">{{ props.name }}</p>
    </Toggle>
</template>

<style scoped>

</style>