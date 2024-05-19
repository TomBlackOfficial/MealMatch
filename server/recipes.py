import os

from flask import Blueprint
from openai import OpenAI

bp = Blueprint("recipes", __name__, url_prefix="/recipes")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": """
You are a helpful assistant designed to output JSON.
"""}


@bp.route("/", methods=("GET",))
def generate_recipes(
        cuisine: list | None = None,
        ingredients: list | None = None,
        preferences: list | None = None,
        restrictions: list | None = None,
    ):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            FIRST_SYSTEM_MESSAGE,
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    )
    return response.choices[0].message.content
