# Programma,  kas HTML veidnē pieprasa ievadīt vārdu un uzvārdu, to saglabā kā teksta failu personas.txt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('p1.html')

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        # Saglabājam vārdu un uzvārdu teksta failā
        with open('personas.txt', 'a') as file:
            file.write(f'{first_name} {last_name}\n')
        
        return 'Dati saglabāti veiksmīgi!'

if __name__ == '__main__':
    app.run(debug=True)