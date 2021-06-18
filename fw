from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/me/")
def lunch():
    menu = ["pet.png", "school.png", "food.png"]
    pickme = random.choice(menu)
    return render_template('index.html', tci=pickme)
if __name__ == "__main__":
    app.run(debug=True)
