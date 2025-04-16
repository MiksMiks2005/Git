from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)
@app.route('/')
def Majas():
    return render_template('Majas.html')
@app.route('/Par/')
def Par():
    teksts = []
    with open(r'C:\Git\Projekta_darbs\abuut.txt', 'r',encoding='utf-8') as file:
        for line in file:
            teksts.append(line.strip())
    return render_template('About.html', names=teksts)

@app.route('/zinas')
def zinas():
    response = requests.get("https://wttr.in/?format=3")
    if response.status_code == 200:
        weather_data = response.text
        return render_template('Palidzet.html', teksts=weather_data)
    else:
        return "Nevarēja iegūt Gadalaiku"
if __name__ == '__main__':
    app.run(debug=True)

