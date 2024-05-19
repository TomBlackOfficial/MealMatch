<script setup lang="ts">
import {useCreateRecipeStore} from "~/store/createRecipe";

const store = useCreateRecipeStore();

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

let { data } = await useFetch<RecipeSuggestions>("http://127.0.0.1:5000/recipes/suggestions", {
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

data = JSON.parse(data.value);

console.log(data);
</script>

<template>
<div class="flex bg-[#FFE9E2]">
  <main class="container m-auto flex flex-col gap-4 justify-center items-center mt-10">
    <img class="fixed z-50 -right-6 -bottom-56 scale-50" src="~/assets/images/Mascot_4.png">
    <div class="grid grid-cols-2 gap-4 w-2/3">
      <Card class="px-4 py-10 rounded-2xl" v-for="recipe in data!.validRecipes" :key="recipe.name">
      <CardContent>
        <b class="text-2xl">{{ recipe.name }}</b>
        <p>{{ recipe.shortDescription }}</p>
        <div class="grid grid-cols-2 mt-10">
          <div>
            <b>Main Ingredients</b>
            <p v-for="ingredient in recipe.mainIngredients" :key="ingredient">{{ ingredient }}</p>
          </div>
          <div>
            <b>Nutrition</b>
            <p>Calories: {{ recipe.nutrition.calories }}</p>
            <p>Protein: {{ recipe.nutrition.protein }}</p>
            <p>Carbohydrates: {{ recipe.nutrition.carbohydrates }}</p>
            <p>Fat: {{ recipe.nutrition.fat }}</p>
          </div>
        </div>

      </CardContent>
    </Card>
    </div>
  </main>
</div>
</template>

<style scoped>

</style>