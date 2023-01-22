from flask import Flask, render_template as rt


app = Flask(__name__)


@app.get("/fizzbuzz")
def get_fizzbuzz():
    return rt("fizzbuzz.html")
