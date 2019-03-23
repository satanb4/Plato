import sqlite3 as sq

class Database:

    def __init__(self):
        global conn
        global cur
        conn = sq.connect(r"/static/user_data.db")
        cur = conn.cursor()
        cur.executescript(
            "CREATE TABLE IF NOT EXISTS users(sid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,fname TEXT,sname TEXT,mail TEXT,password VARCHAR); \
            CREATE TABLE IF NOT EXISTS academics(aid INTEGER,class INTEGER,school TEXT,city TEXT, PRIMARY KEY(aid),FOREIGN KEY(aid) REFERENCES users(sid) ON DELETE CASCADE); \
            CREATE TABLE IF NOT EXISTS achievements(uid INTEGER,points INTEGER, level INTEGER,PRIMARY KEY(uid),FOREIGN KEY(uid) REFERENCES users(sid) ON DELETE CASCADE);\
            CREATE TABLE IF NOT EXISTS topics(tid INTEGER PRIMARY KEY, topic TEXT)"
        )
        """
        cur.execute(
            "CREATE TABLE IF NOT EXISTS academics(sid INTEGER FOREIGN KEY(sid) REFERENCES users(sid),class INT,school TEXT,city TEXT)"
        )"""
        conn.commit()
    
    def add_user(self,fname,sname,mail,password):
        error = None
        cur.execute(
            "INSERT INTO TABLE users(NULL,?,?,?,?,?)",(fname,sname,mail,password)
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
    
    def update_users(self,sid,fname,sname):
        error = None
        cur.execute(
            "UPDATE academics SET fname=?,sname=? WHERE sid=?",(fname,sname,sid)
        )
        conn.commit()
        if error != None:
            conn.rollback()

    def update_academics(self,sid,classs,school,city):
        error = None
        cur.execute(
            "UPDATE academics SET class=?,school=?,city=? WHERE sid=?",(classs,school,city,sid)
        )
        conn.commit()
        if error != None:
            conn.rollback()
    
    def update_achievements(self,sid,points,level):
        error = None
        
        cur.execute(
            "UPDATE achievements SET points=?,level=? WHERE sid=?",(points,level,sid)
        )
        conn.commit()
        if error != None:
            conn.rollback()

    def view_users(self,sid):
        cur.execute(
            "SELECT fname,sname,birthday,mail FROM users WHERE sid=?",(sid)
        )
        rows = cur.fetchall()
        return rows
    
    def login_check(self,mail):
        cur.execute(
            "SELECT id FROM users WHERE mail=?",(mail)
        )
        rows = cur.fetchall()
        return rows
    
    def view_academics(self,sid):
        cur.execute(
            "SELECT * FROM academics WHERE sid=?",(sid)
        )
        rows = cur.fetchall()
        return rows
    
    def __del__(self):
        conn.close()
