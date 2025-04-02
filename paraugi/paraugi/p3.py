#anekdotes no API vietnes https://sv443.net/jokeapi/v2/, API tiek ģenerēts pēc 
# uztādījumiem, izvēlamies txt formātu
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def anekdotes():
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,racist,sexist&format=txt&type=single")
    if response.status_code == 200:
        joks = response.text
        return render_template('p3.html', teksts=joks)
    else:
        return "Nevarēja iegūt joku"

if __name__ == '__main__':
    app.run(debug=True)
