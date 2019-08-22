import sqlite3


conn = sqlite3.connect("my-db.sqlite")
res = conn.execute("SELECT * FROM student;")

print(list(res))

