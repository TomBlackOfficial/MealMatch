import os

from flask import Blueprint
from openai import OpenAI

bp = Blueprint("recipes", __name__, url_prefix="/recipes")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": """You are a professional nutritionist who is creating a meal plan for a client. The client will provide a detailed list of criteria.
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


@bp.route("/", methods=("GET",))
def generate_recipes(
        cuisine: list[str] | None = None,
        ingredients: list[str] | None = None,
        preferences: list[str] | None = None,
        restrictions: list[str] | None = None,
        cooking_method: str | list[str] | None = "Any",
        cost: str | None = "Average",
        cooking_time: str | None = "Average",
        skill_level: str | None = "Intermediate",
) -> str:
    if ingredients is None:
        ingredients = ["chicken", "rice", "broccoli"]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        max_tokens=2000,
        response_format={"type": "json_object"},
        messages=[
            FIRST_SYSTEM_MESSAGE,
            {
                "role": "user",
                "content": f"""Cuisine: {cuisine}
Ingredients: {ingredients}
Preferences: {preferences}
Restrictions: {restrictions}
Cost: {cost}
Cooking Time: {cooking_time}
Skill Level: {skill_level}
Cooking Method: {cooking_method}"""
            }
        ]
    )
    print(response.usage.to_dict())
    return response.choices[0].message.content
