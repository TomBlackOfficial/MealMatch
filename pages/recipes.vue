<script setup lang="ts">
import {useCreateRecipeStore} from "~/store/createRecipe";

const store = useCreateRecipeStore();

async function getAiResponses() {
    let cuisine = [];
    let restrictions = [];
    let appliances = [];

    if (store.american) {
        cuisine.push("American");
    }
    if (store.chinese) {
        cuisine.push("Chinese");
    }
    if (store.japanese) {
        cuisine.push("Japanese");
    }
    if (store.indian) {
        cuisine.push("Indian");
    }
    if (store.greek) {
        cuisine.push("Greek");
    }
    if (store.mexican) {
        cuisine.push("Mexican");
    }
    if (store.italian) {
        cuisine.push("Italian");
    }
    if (store.thai) {
        cuisine.push("Thai");
    }
    if (store.vietnamese) {
        cuisine.push("Vietnamese");
    }
    if (store.korean) {
        cuisine.push("Korean");
    }


    if (store.vegan) {
        restrictions.push("Vegan");
    }
    if (store.vegetarian) {
        restrictions.push("Vegetarian");
    }
    if (store.pescatarian) {
        restrictions.push("Pescatarian");
    }
    if (store.kosher) {
        restrictions.push("Kosher");
    }
    if (store.halal) {
        restrictions.push("Halal");
    }
    if (store.keto) {
        restrictions.push("Keto");
    }
    if (store.dairyFree) {
        restrictions.push("Dairy-Free");
    }
    if (store.glutenFree) {
        restrictions.push("Gluten-Free");
    }
    if (store.nutFree) {
        restrictions.push("Nut-Free");
    }
    if (store.shellfishFree) {
        restrictions.push("Shellfish-Free");
    }
    if (store.eggFree) {
        restrictions.push("Egg-Free");
    }
    if (store.soyFree) {
        restrictions.push("Soy-Free");
    }

    if (store.oven) {
        appliances.push("Oven");
    }
    if (store.microwave) {
        appliances.push("Microwave");
    }
    if (store.airFryer) {
        appliances.push("AirFryer");
    }
    if (store.stove) {
        appliances.push("Stove");
    }
    if (store.BBQ) {
        appliances.push("BBQ");
    }
    if (store.slowCooker) {
        appliances.push("Slow Cooker");
    }
    if (store.blender) {
        appliances.push("Blender");
    }
    if (store.pressureCooker) {
        appliances.push("Pressure Cooker");
    }

    const data = await $fetch("http://127.0.0.1:5000/recipes/suggestions", {
        method: "GET",
        query: {
            cuisine: cuisine,
            restrictions: restrictions,
            cost: store.cost,
            time: store.time,
            skill: store.skill,
            cooking_method: appliances
        },
    });

    console.log(data);
}

await getAiResponses();
</script>

<template>

</template>

<style scoped>

</style>