from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from markupsafe import escape

app = Flask(__name__)

# Secure Secret Key
app.secret_key = os.getenv("SECRET_KEY", "ChangeThisInProduction")

connection = sqlite3.connect("users.db", check_same_thread=False)
cursor = connection.cursor()


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        query = "SELECT * FROM users WHERE username=?"

        cursor.execute(query, (username,))

        user = cursor.fetchone()

        if user:

            stored_hash = user[2]

            if check_password_hash(stored_hash, password):

                session["user"] = username

                return redirect("/home")

        return "Invalid Username or Password"

    return render_template("login.html")


@app.route("/home")
def home():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "home.html",
        username=escape(session["user"])
    )


@app.route("/search")
def search():

    keyword = request.args.get("q", "")

    return render_template(
        "search.html",
        keyword=escape(keyword)
    )


if __name__ == "__main__":

    app.run(debug=False)
    