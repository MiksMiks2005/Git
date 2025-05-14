from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
@app.route('/')
def home():
    response = requests.get("https://wttr.in/?format=4")
    if response.status_code == 200:
        weather_data = response.text
        return render_template('home.html', teksts=weather_data)
    else:
        return "Nevarēja iegūt Gadalaiku"
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/Albumi')
def Albumi():
    return render_template('Albumi.html')
@app.route('/Veikals')
def Veikals():
    return render_template('Veikals.html')
if __name__ == '__main__':
    app.run(debug=True)
