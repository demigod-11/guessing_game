from flask import Flask, render_template, request, url_for, redirect, session
from flask_session import Session
from tempfile import mkdtemp
from game import *

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # checks if user is logged in
        if not session:
            return redirect("/login")
        else:
            name = session["user_id"]
            return render_template("index.html" ,name=name)
    else:
        # checks which post request was sent
        if request.form.get("dex") == "Rules": 
            return redirect("/rules")
        else:
            return redirect("/play")
      
    
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Remember which user has logged in
        session["user_id"] = request.form.get("username")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/win")
def win():
    ''' displays if guess is found'''
    return render_template("win.html")

@app.route("/rules", methods=["GET", "POST"])
def rules():
    ''' displays rules of the game'''
    if request.method == "POST":
        return redirect("/play")

    return render_template("rules.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    ''' guessing game'''
    name = session["user_id"]
    answer = True
    if request.method == "POST":
        if request.form.get("req") == "Correct":
            answer = False
            return render_template("win.html", answer=answer, name=name)
        elif request.form.get("req") == "Play Again":
            return redirect("/play")
    else:
        return render_template("play.html", answer=answer, name=name)

