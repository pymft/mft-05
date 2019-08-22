import sqlite3


conn = sqlite3.connect("my-db.sqlite")
conn.execute("""
CREATE TABLE IF NOT EXISTS records (
  id INTEGER PRIMARY KEY AUTOINCREMENT ,
  username TEXT NOT NULL, 
  weight REAL,
  height REAL
);""")

conn.close()