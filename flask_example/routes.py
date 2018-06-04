from flask_example import flask_example

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"