import sqlite3
from flask import Flask, render_template, request

app = Flask("my-app")


def create_db():
    with sqlite3.connect("my-db.sqlite") as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
          id INTEGER PRIMARY KEY AUTOINCREMENT ,
          username TEXT NOT NULL, 
          weight REAL,
          height REAL
        );""")


def insert_data(username, weight, height):
    with sqlite3.connect("my-db.sqlite") as conn:
        conn.execute(f"""
        INSERT INTO records
          (username, weight, height) VALUES 
          ("{username}", {weight}, {height});
        """)
        conn.commit()


def get_user_records(username):
    with sqlite3.connect("my-db.sqlite") as conn:
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
