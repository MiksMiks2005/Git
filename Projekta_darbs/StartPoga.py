from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
@app.route('/')
def Majas():
    return render_template('Majas.html')
@app.route('/Par/')
def Par():
    return render_template('About.html')
@app.route('/zinas')
def zinas():
    return render_template('Palidzet.html', teksts=weather_data)
if __name__ == '__main__':
    app.run(debug=True)

