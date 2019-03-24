from flask import Flask, render_template, redirect, url_for, request, session
from backend import Database
import sqlite3
# from flask-socketio import SocketIO
import random
from flask_bcrypt import Bcrypt


app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = "JajtuBhp25@nfoioet"
# socketio = SocketIO(app)
bcrypt = Bcrypt(app)


@app.route("/", methods=["GET"])
def home():
    try:
        if not session['logged_in']:
            return redirect(url_for("signup"))
        else:
            lwe = ["Calculus", "English", "Statistics"]
            return render_template("home.html", name="sayan", topics=lwe)
    except Exception:
        return redirect(url_for("signup"))

@app.route("/login", methods=["GET", "POST"])
def login():
	db = Database()
	if request.method == 'POST':
		dbmail = request.form.get('mail')
		
		"""
        with sqlite3.connect(r"user_data.db") as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users(sid INTEGER PRIMARY KEY,fname TEXT,sname TEXT,mail TEXT,password VARCHAR);")
            conn.commit()
			cur.execute("SELECT sid,fname,sname,password FROM users WHERE mail=?",(dbmail,))
			rows = cur.fetchall()
		"""

		passw = db.view_users(dbmail)[0][3]
		user = db.view_users(dbmail)[0][1] 
		if passw == request.form.get('pass'):
			session['logged_in'] = True
			return redirect(url_for("home"))
		else:
			return render_template("login.html")
	else:
		return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    db = Database()    
    if request.method == 'POST':
        fname = request.form.get('fname')
        sname = request.form.get('sname')
        mail = request.form.get('mail')
        pword = request.form.get('password')
        # with sqlite3.connect(r"user_data.db") as conn:
        #         cur = conn.cursor()
        #         cur.execute("CREATE TABLE IF NOT EXISTS users(sid INTEGER PRIMARY KEY,fname TEXT,sname TEXT,mail TEXT,password VARCHAR);")
        #         cur.execute("INSERT INTO users VALUES(NULL,?,?,?,?)",(fname,sname,mail,pword))
        #         conn.commit()
        db.add_user(fname,sname,mail,pword)
        session['logged_in'] = True
        return redirect(url_for("home"))
    else:
        return render_template("signup.html")

@app.route("/logout")
def logout():
        session['logged_in'] = False
        return redirect(url_for("home"))

@app.route("/quiz")
def quiz():
        total=["Lorem Ipsum","DOLOR","CATCH ME IF YOU CAN"]
        return render_template("chat.html",quiz = total)


if __name__ == "__main__":
    app.run(debug=True)
