import os

from flask import Blueprint, request
from openai import OpenAI

bp = Blueprint("recipes", __name__, url_prefix="/recipes")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

RECIPE_SUGGESTIONS_SYSTEM_MESSAGE = {"role": "system", "content": """You are a professional nutritionist who is creating a meal plan for a client. The client will provide a detailed list of criteria.
Generate a list of ten unique recipes that match these criteria. The names should be descriptive and appetizing, reflecting the meal type, cuisine, dietary restrictions, cost, preparation time, and skill level.
The recipes must use the ingredients provided and match the client's preferences. The client's dietary restrictions must be followed.
Additionally, generate five more recipes that could be made with up to 3 ingredients not provided on the list.
Return your responses in a JSON object with the following format:
{
  "validRecipes": [
    {
      "name": "Recipe Name",
      "shortDescription": "Short Recipe Description",
    }
  ]
  "additionalRecipes": [
    {
      "name": "Recipe Name",
      "shortDescription": "Short Recipe Description",
    }
  ]
}
"""}

RECIPE_DETAILS_SYSTEM_MESSAGE = f"""You are a professional nutritionist who is creating a meal plan for a client. The client will provide a name of a recipe and a short description that was generated based on a detailed list of criteria.
Generate a the full list of ingredients and instructions for the recipe. The recipe should match the client's preferences and dietary restrictions.
Return your response in a JSON object with the following format:
{
  "name": "Recipe Name",
  "ingredients": ["Ingredient Name 1 and Quantity", "Ingredient Name 2 and Quantity", ...],
  "instructions": ["Step 1", "Step 2", "Step 3", ...]
  "cookingTime": "Cooking Time",
}
"""


@bp.route("/suggestions", methods=("GET",))
def get_recipe_suggestions():
    args = request.args
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        max_tokens=2000,
        response_format={"type": "json_object"},
        messages=[
            RECIPE_SUGGESTIONS_SYSTEM_MESSAGE,
            {
                "role": "user",
                "content": f"""Cuisine: {args.get("cuisine", default="Any")}
Ingredients: {args.get("ingredients", default="Any")}
Preferences: {args.get("preferences", default="Any")}
Restrictions: {args.get("restrictions", default="None")}
Cost: {args.get("cost", default="Average")}
Cooking Time: {args.get("cooking_time", default="Average")}
Skill Level: {args.get("skill_level", default="Intermediate")}
Cooking Method: {args.get("cooking_method", default="Any")}"""
            }
        ]
    )
    print(response.usage.to_dict())
    return response.choices[0].message.content


@bp.route("/details", methods=("GET",))
def get_recipe_details():
    args = request.args
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        max_tokens=2000,
        response_format={"type": "json_object"},
        messages=[
            RECIPE_DETAILS_SYSTEM_MESSAGE,
            {
                "role": "user",
                "content": f"""Name: {args.get("name", default="Chicken Alfredo")}
Description: {args.get("description", default="A creamy pasta dish with chicken and broccoli.")}
Ingredients: {args.get("ingredients", default="Any")}
Preferences: {args.get("preferences", default="Any")}
Restrictions: {args.get("restrictions", default="None")}
Cost: {args.get("cost", default="Average")}
Cooking Time: {args.get("cooking_time", default="Average")}
Skill Level: {args.get("skill_level", default="Intermediate")}
Cooking Method: {args.get("cooking_method", default="Any")}"""
            }
        ]
    )
    print(response.usage.to_dict())
    return response.choices[0].message.content
