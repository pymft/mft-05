import flask

app = flask.Flask("app")


@app.route('/')
def index():
    return "Hello"


@app.route('/login')
def login():
    return "Login"


@app.route('/greeting/<name>')
def greeting(name=""):
    return "Hello " + name


app.run(port=8000)
