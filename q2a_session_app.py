from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "lab_secret_key"

@app.route("/login")
def login():
    session["user"] = "admin"
    return "Logged in! Go to <a href='/dashboard'>/dashboard</a>"

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return f"<h2>Dashboard - Welcome {session['user']}</h2>"
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
