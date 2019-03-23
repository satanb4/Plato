from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def home():
        return render_template("login.html")

@app.route("/forgot")
def forgot():
        return render_template("forgot.html")
        
@app.route("/signup")
def signup():
        return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug = True)