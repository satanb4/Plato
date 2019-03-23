from flask import Flask, render_template, redirect, url_for, request
<<<<<<< HEAD
#import backend as dbHandler
=======
from flask_socketio import SocketIO
import random

>>>>>>> 4e51dcb8bf020a83d165526bf1f41a88cb56a293

app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = "JajtuBhp25@nfoioet"
# socketio = SocketIO(app)

@app.route("/")
def home():
     return render_template('landing.html')



@app.route("/login", methods = ['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		
		mail = request.form('mail')
		password = request.form('password')
			
		for row in dbHandler.view_user(mail):
			dbMail = row[0]
			dbPass = row[1]
			if dbUser == mail:
				completion = dbHandler.check_password(dbPass, password)
				if(completion):

					return render_template('index.html', users = row[0])

				else:

					 error = 'Invalid Credentials'
		
			else:

				error = 'Invalid Credentials'

		return render_template('index.html', users = users, errors = error)

	else:
		return render_template('login.html')

@app.route("/register", methods = ['GET','POST'])
def register():
	if request.method == 'POST':

		fname = request.form('fname')
		sname = request.form('sname')
		mail = request.form('mail')
		password = request.form('password')
		hashed_pass = hashlib.md5(user_password.encode()).hexdigest()
		dbHandler.add_user(fname,sname,mail,hashed_pass)
		users = dbHandler.view_user(mail, password)
		return render_template('index.html', users = users[0])

	else:

		return render_template('register.html')

@app.route("/ocr")
def ocr():
	l = ['Exhibitor Survey\n\n‘About the Your EOD6 Experience\n\n1. Did you attend any educational sessions at ECO6 (eg, Menday/Tesay Training Courses, Wedneslay!\n“Thursliy Techical Sesons Feld DayartheBeah', ' C1Yes [No\n\n2. Did you stay at an IECA Host Hote', ' Cis Skip gueionts No\n\n43. Ifyou didnot say 2 an ECA Host Howl, why not', ' Mar. mon\n\ntxeaion CiPeine pogamacosherhard — C1 Goxe Cotter\n\n4. £006 expo mas open for 14 hous over 3 days. Ithink the number ofhours shoud be: Plc chne ate\nOneal deceased (ieee same fo change)\n\nComme:\n\n5. Rate the exhibitor lounge: Plas mer one\n\nCxetene Oona Daverge Poe\nComme:\n\n(6, What would you lke tose inthe exhibitor lounge', ' Mark many a apy.\nCmeniewRoom — ClLunch Education Clmemet.—C1Sada—-C1.Room fr Press\nConfsences\nOther\n\n7. Would you be willing to pay additonal booth fees ifthese services were offred', '’ CIYes (No\n8 Which hour did yousce the most traffic Wednesday', ' Plane chao\n\nOttam-tp D13pm Os5pm 015-6:30pm\n\n9. Which hours did you see the mos trafic Thursday', ' ae cvac on\n\nCttan-tpm O1jpm Os4pm,\n\n10, Did youmectsufcent number of qualified buyers', ' Ya C)No\n\n11, Would you exhibit at another IECA conference', ' Ye stiproquesin #13 CONo\n12, Why would’ you exhibit t another IECA conference', '']
	return render_template("ocrdisplay.html",li=l)

@app.route("/forgot")
def forgot():
        return render_template("forgot.html")

@app.route("/signup")
def signup():
        return render_template("signup.html")

@app.route("/quiz")
def quiz():
        return render_template("quiz.html")

if __name__ == "__main__":
    app.run(debug = True)

