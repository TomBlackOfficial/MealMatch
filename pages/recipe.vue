<script setup lang="ts">

const recipe = await useFetch<RecipeCriteria>("http://localhost:5000/recipes/suggestions", {
        query: {

        }
    })
</script>

<template>

</template>

<style scoped>

</style>