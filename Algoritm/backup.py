import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    id = session["user_id"]


    stocks = db.execute("SELECT * FROM portfolio WHERE user_id = ?", id)

    # get user cash
    cash = db.execute("SELECT cash from users WHERE id = ?", id)



    totalPrice = cash[0]['cash']
    for stock in stocks:
       # look =  lookup(stock['symbol'])
        #stock['name'] = look[0]['name']
        stock['total'] = stock['price'] * stock['shares']

        # increment totalPrice
        totalPrice += stock['total']

    return render_template("index.html", stocks=stocks, cash=cash, total=totalPrice)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":

       symbol =  request.form.get("symbol")

       if not symbol or symbol == None:
        return apology("No Valid Symbol !")

       shares = request.form.get("shares")

       if not shares or not shares.isdigit():
        return apology("Not a valid Share", 400)

       if (int(shares) <= 0):
        return apology("Shares is not positive, enter a postiive number of shares", 400)

       shares = int(shares)

       #validate lookup symbol
       symbol = lookup(symbol)
       if symbol == None:
        return apology("Not a valid symbol !", 400)

       # get total price
       totalPrice = symbol['price'] * shares

       id = session["user_id"]

       # get username from database
       username = db.execute("SELECT username FROM users where id = ?",id)
       username = username[0]['username']

       # See how much user has in hands
       result = db.execute("SELECT cash FROM users WHERE id = ?", id)
       owned = result[0]['cash']

       # check if he can buy
       if owned < totalPrice:
        return apology("User cannot afford that amount.",400)

       #owe = owned - totalPrice

       # query portfolio which is owned table for row with this userid and stock symbol:
       check = db.execute("SELECT * from portfolio WHERE user_id = ? AND symbol = ?", id, symbol['symbol'])

       # if do not exist, insert new data
       if len(check) != 1:
        db.execute("INSERT INTO portfolio (user_id, symbol, name, price) VALUES(?, ?, ?, ?)", id, symbol['symbol'], symbol['name'], symbol['price'])

       # get owned  amount of shares
       userShares = db.execute("SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ?", id, symbol['symbol'])
       userShares = userShares[0]['shares']

       # Add buyed shares to use in update
       updatedShares = shares + userShares

       # Add shares into portfolio table
       db.execute("UPDATE portfolio SET shares = ? WHERE user_id = ? AND symbol = ?", updatedShares, id, symbol['symbol'])

       # Decrease value from cash table
       db.execute("UPDATE users SET cash = cash - ?  WHERE id = ?", totalPrice, id)

       # Insert in history log
       db.execute("INSERT INTO history VALUES(?, ?, ? , ?, ?, ?, ?, DateTime('Now'))", id, username, symbol['name'], symbol['symbol'], shares, symbol['price'], "Buy")
       return redirect("/")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    id = session["user_id"]

    logs = db.execute("SELECT * from history WHERE user_id = ?", id)

    return render_template("history.html", logs=logs)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    search = {}
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Please Insert a valid Symbol")

        results = lookup(symbol)

        if not results:
            return apology("Symbol not founded", 400)

        return render_template("quoted.html", results=results)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

         if not request.form.get("username"):
            return apology("must provide username", 400)

         elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide a valid password", 400)

         username = request.form.get("username")
         password = request.form.get("password")
         confirmation = request.form.get("confirmation")


        # check if already exists username
         usercheck = []
         usercheck = db.execute("SELECT username from users WHERE username = ?",username)
         if len(usercheck) == 1:
            if username == usercheck[0]['username']:
                return apology("User already registered", 400)

        # Testar Registro com mesmo Usuario

         if password != confirmation:
            return apology("Passwords do not match !", 400)

         passwordHash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
         db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, passwordHash)
         return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        id = session["user_id"]
        symbols = db.execute("SELECT symbol from portfolio where user_id = ?", id)
        return render_template("sell.html", symbols=symbols)
    else:
        id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate Symbol
        if not symbol:
            return apology("Must provide an symbol !", 400)

        if not shares:
            return apology("Must provide a share !", 400)

        stock = lookup(symbol)
        if not stock:
            return apology("Symbol not valid", 400)

        # Validate shares
        if int(shares) <= 0:
            return apology("Share it's not a positive integer", 400)

        # Check if user has that amount of shares
        ownedShares = db.execute("SELECT shares FROM portfolio where user_id = ? AND symbol = ?", id, symbol)

        # check if the shares are less or equals to the portfolio table
        if int(shares) <= ownedShares[0]['shares']:
            # get username
            username = db.execute("SELECT username FROM users where id = ?", id)
            username = username[0]['username']

            # get the total price to be selled
            totalPrice = stock['price'] * int(shares)

            # Updates cash to the user table
            db.execute("UPDATE users set CASH = cash +  ? WHERE id = ?", totalPrice, id)

            # decrease from portfolio
            db.execute("UPDATE portfolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?", shares, id, symbol)

            # delete row from portfolio if shares is 0
            db.execute("delete FROM portfolio WHERE user_id = ? AND symbol = ? AND shares = 0", id, symbol)

            int(shares)

            # Add to history log
            db.execute("INSERT INTO history VALUES(?, ?, ? , ?, ?, ?, ?, DateTime('Now'))", id, username, stock['name'], stock['symbol'], shares, stock['price'], "Sell")

            return redirect("/")

        else:
            return apology("User doenst have that amount of shares to sell.", 400)

# Add Cash Personal Touch


@app.route("/addCash", methods=["GET", "POST"])
def addCash():
    if request.method == "GET":
        return render_template("addCash.html")
    else:
        cash = int(request.form.get("cash"))

        # validate cash input
        if not cash:
            return apology("Must provide a valid value !", 400)

        if cash <= 0:
            return apology("Must provide a positive number !", 400)

        id = session["user_id"]

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", cash, id)
        return redirect("/")


@app.route("/changePassword", methods=["GET", "POST"])
def changePassword():
    if request.method == "GET":
        return render_template("changePassword.html")
    else:
        oldPassword = request.form.get("oldPassword")
        newPassword = request.form.get("newPassword")

        if not oldPassword or not newPassword:
            return apology("Must provide a valid password !", 400)

        id = session["user_id"]
        checkPassword = db.execute("SELECT hash from users WHERE id = ?", id)

        if check_password_hash(checkPassword[0]['hash'], oldPassword) == False:
            return apology("Your password do not match!", 400)
        return redirect("/")
