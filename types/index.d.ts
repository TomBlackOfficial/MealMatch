declare global {
    interface UserDetails {
        cuisine: string,
        ingredients: string[],
        preferences: string[],
        restrictions: string[],
        cost: string,
        cookingTime: string,
        skillLevel: string,
        cookingMethod: string,
    }

    interface RecipeSuggestions {
        validRecipes: {
            name: string,
            shortDescription: string,
        }[],
        additionalRecipes: {
            name: string,
            shortDescription: string,
        }[],
    }

    interface RecipeCriteria {
        name: string,
        shortDescription: string,
        ingredients: string[],
        preferences: string[],
        restrictions: string[],
        cost: string,
        cookingTime: string,
        skillLevel: string,
        cookingMethod: string,
    }

    interface RecipeDetails {
        name: string,
        ingredients: string[],
        instructions: string[],
        cookingTime: string,
    }
}