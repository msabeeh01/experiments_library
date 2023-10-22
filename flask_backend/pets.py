from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def getPets():
    if request.method == "GET":
        return 'pets go here 2'