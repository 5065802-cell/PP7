from datetime import timedelta
from flask import Flask, session

app = Flask(__name__)
app.secret_key = "lab_secret_key"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/login")
def login():
    session.permanent = True
    session["user"] = "admin"
    return "Permanent session started (expires in 5 minutes). Check <a href='/status'>/status</a>."

@app.route("/status")
def status():
    return f"Active user: {session.get('user', 'Session Expired / None')}"

if __name__ == "__main__":
    app.run(debug=True)
