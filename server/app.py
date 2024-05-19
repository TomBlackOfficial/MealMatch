from flask import Flask
from flask_cors import CORS

import recipes

app = Flask(__name__)
app.register_blueprint(recipes.bp)
CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "localhost:3000"
    }
})


@app.route("/", methods=("GET",))
def main():
    return {"response": "Hello World!"}
