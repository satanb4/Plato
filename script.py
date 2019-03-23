from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO
import random


app = Flask(__name__, static_url_path="/static")
app.config['SECRET_KEY'] = "JajtuBhp25@nfoioet"
# socketio = SocketIO(app)

@app.route("/")
def home():
        return render_template("login.html")

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