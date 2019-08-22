import sqlite3
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

def create_db():
    conn = sqlite3.connect("my-db.sqlite")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS records (
      id INTEGER PRIMARY KEY AUTOINCREMENT ,
      username TEXT NOT NULL, 
      weight REAL,
      height REAL
    );""")

    conn.close()

def insert_data(username, weight, height):
    conn = sqlite3.connect("my-db.sqlite")
    conn.execute(f"""
    INSERT INTO records
      (username, weight, height) VALUES 
      ("{username}", {weight}, {height});
    """)
    conn.commit()


def get_user_records(username):
    conn = sqlite3.connect("my-db.sqlite")
    res = conn.execute(f"""
        SELECT *, weight/height/height FROM records WHERE username = "{username}";
    """)
    return list(res)


@app.route("/cool", methods=["GET", "POST"])
def cool():
    if request.method == 'GET':
        return render_template("cool.html")
    else:
        username = request.form['username']
        weight = float(request.form['w'])
        height = float(request.form['h'])
        bmi = weight / height ** 2

        insert_data(username, weight, height)
        recs = get_user_records(username)

        return render_template("cool.html", bmi=bmi, recs=recs)


if __name__ == '__main__':
    create_db()
    app.run()
