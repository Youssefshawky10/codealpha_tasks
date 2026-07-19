from flask import *

import sqlite3

import hashlib

app = Flask(__name__)

# Vulnerability 1

app.secret_key = "my-secret-key"

connection = sqlite3.connect("users.db",check_same_thread=False)

cursor = connection.cursor()


@app.route("/",methods=["GET","POST"])

def login():

    if request.method=="POST":

        username=request.form["username"]

        password=request.form["password"]

        hashed=hashlib.md5(password.encode()).hexdigest()

        # Vulnerability 2

        query=f"SELECT * FROM users WHERE username='{username}' AND password='{hashed}'"

        cursor.execute(query)

        user=cursor.fetchone()

        if user:

            session["user"]=username

            return redirect("/home")

        else:

            return "Login Failed"

    return render_template("login.html")


@app.route("/home")

def home():

    if "user" not in session:

        return redirect("/")

    return render_template(

        "home.html",

        username=session["user"]

    )


@app.route("/search")

def search():

    keyword=request.args.get("q","")

    # Vulnerability 3

    return f"<h2>Results for {keyword}</h2>"


if __name__=="__main__":

    # Vulnerability 4

    app.run(debug=True)