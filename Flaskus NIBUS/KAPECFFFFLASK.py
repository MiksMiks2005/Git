from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<html><body><h1>Hello World</h1></body></html>"
@app.route("/hello")
@app.route('/hello/')
def hello_name(name):
   return 'Hello %s!' % name
if name == '__main__':
    app.run(debug=True)