from flask import Flask, render_template, redirect, url_for, request, session
from backend import Database
#from flask-socketio import SocketIO 
import random
from flask_bcrypt import Bcrypt


app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = "JajtuBhp25@nfoioet"
# socketio = SocketIO(app)
bcrypt = Bcrypt(app)

@app.route("/")
def home():
	return render_template('signup.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	db = Database()
	if request.method == 'POST':
		if bcrypt.check_password_hash(db.login_check(request.form['mail']), request.form['password']):
			session['logged_in']=True
			return render_template("home.html")
		else:
			return("login.html")
	else:
		return("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
	db = Database()
	if request.method == 'POST':
		firstname = request.form.get('fname')
		lastname = request.form.get('sname')
		email = request.form.get('mail')
		pword = request.form.get('password')
		db.add_user(firstname,lastname,email,pword)
		return render_template("layout.html")
	else:
		return("signup.html")


if __name__ == "__main__":
    app.run(debug = True)