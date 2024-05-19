<script setup lang="ts">

let { data: recipe } = await useFetch<Object>("http://localhost:5000/recipes/suggestions", {
        query: {
        }
    })
recipe.value! = {
  "name": "Chicken Alfredo",
  "ingredients": [
    "8 oz fettuccine pasta",
    "1 lb chicken breast, cut into bite-sized pieces",
    "2 tbsp olive oil",
    "2 cloves garlic, minced",
    "1 cup broccoli florets",
    "1 cup heavy cream",
    "1 cup grated Parmesan cheese",
    "Salt and pepper to taste",
    "Fresh parsley for garnish"
  ],
  "instructions": [
    "1. Cook the fettuccine pasta according to package instructions. Drain and set aside.",
    "2. In a large skillet, heat the olive oil over medium heat. Add the chicken pieces and cook until they are no longer pink, about 5-7 minutes.",
    "3. Add the minced garlic and broccoli florets to the skillet and sauté for another 3-4 minutes until the broccoli is tender-crisp.",
    "4. Pour in the heavy cream and grated Parmesan cheese. Stir well to combine and let the sauce simmer for 2-3 minutes until it thickens slightly.",
    "5. Add the cooked fettuccine pasta to the skillet and toss to coat the pasta in the creamy sauce.",
    "6. Season with salt and pepper to taste.",
    "7. Serve the chicken alfredo hot, garnished with fresh parsley.",
    "8. Enjoy your creamy pasta dish with chicken and broccoli!"
  ],
  "cookingTime": "30 minutes"
};
</script>

<template>
  <Table>
    <TableCaption></TableCaption>
    <TableHeader>
      <TableRow>
        <TableHead class="w-[100px]">
          Ingredients
        </TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="ingredient in recipe!.ingredients" :key="ingredient"/>
    </TableBody>
  </Table>
</template>

<style scoped>

</style>