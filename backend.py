import sqlite3 as sq

class Database:

    def __init__(self):
        global conn
        global cur
        conn = sq.connect(r"user_data.db")
        cur = conn.cursor()
        cur.executemany(
            "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,fname TEXT,sname TEXT,birthday DATE,mail TEXT); \
            CREATE TABLE IF NOT EXISTS academics(id INTEGER FOREIGN KEY(id) REFERENCES users(id),class INT,school TEXT,city TEXT)"
        )
        """
        cur.execute(
            "CREATE TABLE IF NOT EXISTS academics(id INTEGER FOREIGN KEY(id) REFERENCES users(id),class INT,school TEXT,city TEXT)"
        )"""
        conn.commit()
    
    def add_user(self,fname,sname,birthday,mail):
        error = None
        cur.execute(
            "INSERT INTO TABLE users(NULL,?,?,?,?)",(fname,sname,birthday,mail)
        )
        conn.commit()
        if error != None:
            conn.rollback()
    
    def add_academics(self,classs,school,city):
        error = None
        cur.execute(
            "INSERT INTO TABLE academics(NULL,?,?,?)",(classs,school,city)
        )
        conn.commit()
        if error != None:
            conn.rollback()
    
    def update_users(self,id,fname,sname,birthday):
        error = None
        cur.execute(
            "UPDATE academics SET fname=?,sname=?,birthday=? WHERE id=?",(fname,sname,birthday,id)
        )
        conn.commit()
        if error != None:
            conn.rollback()

    def update_academics(self,id,classs,school,city):
        error = None
        cur.execute(
            "UPDATE academics SET class=?,school=?,city=? WHERE id=?",(classs,school,city,id)
        )
        conn.commit()
        if error != None:
            conn.rollback()

    def view_users(self):
        cur.execute(
            "SELECT * FROM users WHERE id=?",(id)
        )
        rows = cur.fetchall()
        return rows
    
    def view_academics(self,id):
        cur.execute(
            "SELECT * FROM academics WHERE id=?",(id)
        )
        rows = cur.fetchall()
        return rows
    
    def __del__(self):
        conn.close()
