from flask import Flask

app = Flask("my-app")


@app.route("/")
def index():
    with open('main.html') as f:
        return f.read()


@app.route("/login")
def login_pate():
    return "login page"


app.run()