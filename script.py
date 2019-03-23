from flask import Flask, render_template, redirect, url_for, request, session
from backend import Database
# from flask-socketio import SocketIO
import random
from flask_bcrypt import Bcrypt


app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = "JajtuBhp25@nfoioet"
# socketio = SocketIO(app)
bcrypt = Bcrypt(app)


@app.route("/")
def home():
    lwe = ["jlfsd", "jlsdaf", "jerwuuefbc"]
    return render_template("home.html", username="sayan", topics=lwe)


@app.route("/register")
def register():
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    db = Database()
    if request.method == 'POST':
        dbmail = request.form.get('mail')
        rows = db.login_check(dbmail)
        print(rows)
        if rows[3] == request.form.get('pass'):
            session['logged_in'] = True
            return render_template("layout.html")
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
        return render_template("home.html")
    else:
        return("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
