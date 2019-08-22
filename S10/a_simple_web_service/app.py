from flask import Flask, render_template, request

app = Flask("my-app")

#
# @app.route("/")
# def index():
#     return render_template("main.html")
#
#
# @app.route("/login/<name>/<int:var>")
# def login_page(name, var):
#     return render_template("login.html", name=name, var=var)
#
#
# @app.route("/table/<int:cols>/<int:rows>")
# def table(cols, rows):
#     return render_template("table.html", rows=rows, cols=cols)


@app.route("/cool", methods=["GET", "POST"])
def cool():
    if request.method == 'GET':
        return render_template("cool.html")
    else:
        username = float(request.form['username'])
        weight = float(request.form['w'])
        height = float(request.form['h'])
        bmi = weight / height ** 2



        return render_template("cool.html", bmi=bmi)


app.run()
