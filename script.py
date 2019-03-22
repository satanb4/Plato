from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] == placed[0] and request.form['password'] == placed[1]:
            