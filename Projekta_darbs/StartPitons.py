from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('majas.html')
@app.route('/padzilinati/')
def padzilinati():
    teksts = []
    with open(r'Flaskus NIBUS\abuut.txt', 'r',encoding='utf-8') as file:
        for line in file:
            teksts.append(line.strip())
    return render_template('padzilinati.html', names=teksts)

@app.route('/zinas')
def zinas():
    response = requests.get("https://wttr.in/?format=3")
    if response.status_code == 200:
        weather_data = response.text
        return render_template('zinas.html', teksts=weather_data)
    else:
        return "Nevarēja iegūt Gadalaiku"
if __name__ == '__main__':
    app.run(debug=True)

