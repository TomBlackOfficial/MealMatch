from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)
openai_client = OpenAI()


@app.route("/", methods=["GET"])
def hello_world():
    return {"response": "Hello World!"}
