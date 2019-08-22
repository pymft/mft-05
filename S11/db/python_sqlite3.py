import sqlite3


conn = sqlite3.connect("my-db.sqlite")
conn.execute("""
CREATE TABLE IF NOT EXISTS student (
  id INTEGER PRIMARY KEY AUTOINCREMENT ,
  first_name TEXT NOT NULL, 
  last_name TEXT NOT NULL,
  age INTEGER 
);""")

first_name = input("first name:")
last_name = input("last name:")
age = int(input("age:"))

conn.execute(f"""
INSERT INTO student 
  (first_name, last_name, age) VALUES 
  ({first_name}, {last_name}, {age});
""")

conn.commit()
