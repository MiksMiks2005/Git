from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/zinas')
def zinas():
    return render_template('zinas.html')
if __name__ == '__main__':
    app.run(debug=True)

