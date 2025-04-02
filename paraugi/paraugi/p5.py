# programma nolasa failu p5_teksts.txt, teksts tiek izvadīts veidnē p5.html
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/vardi')
def show_names():
    teksts = []
    with open('p5_teksts.txt', 'r',encoding='utf-8') as file:
        for line in file:
            teksts.append(line.strip())
    return render_template('p5.html', names=teksts)

if __name__ == '__main__':
    app.run(debug=True)
