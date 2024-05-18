from flask import Flask
from openai import OpenAI

app = Flask(__name__)
openai_client = OpenAI()


@app.route("/")
def hello_world():
    return {"response": "Hello World!"}
