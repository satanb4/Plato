from flask import Flask, render_template, redirect, url_for, request, session
from backend import Database
# from flask-socketio import SocketIO
import random
from flask_bcrypt import Bcrypt


app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = "JajtuBhp25@nfoioet"
# socketio = SocketIO(app)
bcrypt = Bcrypt(app)

<<<<<<< HEAD
@app.route("/", methods=["GET"])
def home():
	try:
		if not session['logged_in']:
			return render_template("login.html")
		else:
			lwe = ["jlfsd","jlsdaf","jerwuuefbc"]
			return render_template("home.html",username="sayan",topics=lwe)
	except Exception:
		return render_template("signup.html")
=======

@app.route("/")
def home():
    lwe = ["Calculus", "Consonants", "Mechanics"]
    return render_template("home.html", username="sayan", topics=lwe)

>>>>>>> bd75272251579b6d9e2e1dc2cdcacadf9448ae24

@app.route("/register")
def register():
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    db = Database()
    if request.method == 'POST':
        dbmail = request.form.get('mail')
        ide = str(db.id_of_mail(dbmail))
        passw = db.view_users(ide)
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
        firstname = request.form.get('fname')
        lastname = request.form.get('sname')
        email = request.form.get('mail')
        pword = request.form.get('password')
        db.add_user(firstname, lastname, email, pword)
        return redirect(url_for("home"))
    else:
        return render_template("signup.html")


@app.route("/quiz")
def quiz():
	return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)
