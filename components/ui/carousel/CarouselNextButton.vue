<script setup lang="ts">
import {useCarousel} from "~/components/ui/carousel/useCarousel";

const { canScrollNext, scrollNext } = useCarousel();
</script>

<template>
    <Button @click="scrollNext">Next</Button>
</template>

<style scoped>

</style>