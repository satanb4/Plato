import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("user_data.db")
        self.cur = self.conn.cursor()
        self.cur.executescript(
            """CREATE TABLE IF NOT EXISTS users(sid INTEGER PRIMARY KEY,fname TEXT,sname TEXT,mail TEXT,password VARCHAR);
            CREATE TABLE IF NOT EXISTS academics(class INTEGER,school TEXT,city TEXT,aid INTEGER, FOREIGN KEY(aid) REFERENCES users(sid) ON DELETE CASCADE);
            CREATE TABLE IF NOT EXISTS achievements(points INTEGER, level INTEGER,uid INTEGER, FOREIGN KEY(uid) REFERENCES users(sid) ON DELETE CASCADE);"""
        )
        """
        cur.execute(
            "CREATE TABLE IF NOT EXISTS academics(sid INTEGER FOREIGN KEY(sid) REFERENCES users(sid),class INT,school TEXT,city TEXT)"
        )"""
        self.conn.commit()
    
    def add_user(self,fname,sname,mail,password):
        self.cur.execute(
            "INSERT INTO users VALUES(NULL,?,?,?,?)",(fname,sname,mail,password)
        )
        self.conn.commit()
    
    def add_academics(self,classs,school,city):
        self.cur.execute(
            "INSERT INTO academics VALUES(NULL,?,?,?)",(classs,school,city)
        )
        self.conn.commit()
    
    def update_users(self,sid,fname,sname):
        self.cur.execute(
            "UPDATE academics SET fname=?,sname=? WHERE sid=?",(fname,sname,sid)
        )
        self.conn.commit()

    def update_academics(self,sid,classs,school,city):
        self.cur.execute(
            "UPDATE academics SET class=?,school=?,city=? WHERE sid=?",(classs,school,city,sid)
        )
        self.conn.commit()
    
    def update_achievements(self,sid,points,level):
        self.cur.execute(
            "UPDATE achievements SET points=?,level=? WHERE sid=?",(points,level,sid)
        )
        self.conn.commit()


    def view_users(self,mail=""):
        self.cur.execute(
            "SELECT sid,fname,sname,password FROM users WHERE mail=?",(mail,)
        )
        rows = self.cur.fetchall()
        return rows
    
    def view_academics(self,sid):
        self.cur.execute(
            "SELECT * FROM academics WHERE sid=?",(sid)
        )
        rows = self.cur.fetchall()
        return rows[0]
    
    def delete_user(self,sid):
        self.cur.execute(
            "DELETE FROM users WHERE sid=?",(sid)
        )
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

