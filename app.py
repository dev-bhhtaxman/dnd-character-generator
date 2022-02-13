from flask import Flask,jsonify
from helpers import generator

app = Flask(__name__)
@app.route("/the_generator")
def generate_character():
    return jsonify(generator.get_rand_character())

# print(generator.get_rand_character())