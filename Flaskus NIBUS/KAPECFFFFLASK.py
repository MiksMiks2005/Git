from flask import Flask , render_template
app = Flask(__name__)
@app.route('/')
def home():
    return "<html><body><h1>Hello World</h1></body></html>"
@app.route('/hello/')
def hello_name(name):
   return 'Hello %s!' % name
@app.route('/pirmais')
def index():
   return render_template('pirmais.html')
if __name__ == '__main__':
    app.run(debug=True)