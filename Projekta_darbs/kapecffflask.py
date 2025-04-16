def hello_world():
   return ‘hello world’
app.add_url_rule(‘/’, ‘hello’, hello_world)