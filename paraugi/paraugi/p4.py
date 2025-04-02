# komentāri mājas lapai
from flask import Flask, render_template, request

app = Flask(__name__)

# S saraksts, kur glabāsies komentāri
komentari = []

@app.route('/')
def index():
    return render_template('p4.html', comments=komentari)

@app.route('/com', methods=['POST'])
def add_comment():
    if request.method == 'POST':
        jauns_komentars = request.form['komentars']
        komentari.append(jauns_komentars)
        return render_template('p4.html', comments=komentari)

if __name__ == '__main__':
    app.run(debug=True)
