import sqlite3 as sq

class Database:

    def __init__(self):
        conn = sq.connect(r"user_data.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,fname TEXT,sname TEXT,birthday DATE,mail TEXT)"
        )
        cur.execute(
            "CREATE TABLE IF NOT EXISTS academics(id INTEGER, FOREIGN KEY(id) REFERENCES users(id),class INT,school TEXT,city TEXT)"
        )
        conn.commit()
    

db = Database()

