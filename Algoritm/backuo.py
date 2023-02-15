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

    # db em vez de puxar owned vai pxuar history`

    stocks = db.execute("SELECT stock, stockSymbol, sum(stockQty) as stockQty, sum(price), sum(totalPrice) as totalPrice FROM history GROUP BY stockSymbol HAVING user_id = ?", id)

    totalQuery = db.execute("select price from history WHERE user_id = ?", id)

    cash = db.execute("SELECT cash from users WHERE id = ?", id)

    total = totalQuery[0]['totalPrice'] + cash[0]['cash']

    return render_template("index.html", stocks=stocks, cash=cash,total=total)



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
       if not shares:
        return apology("No Valid Shares !")
       if (int(shares) <= 0):
        return apology("Shares is not positive, enter a postiive number of shares")

       #validate lookup
       stock = lookup(symbol)
       if stock == None:
        return apology("Not a valid symbol !", 400)

       # get total price
       totalPrice = float(stock['price']) * float(shares)

       id = session["user_id"]

       # get username from database
       username = db.execute("SELECT username FROM users where id = ?",id)

       # See how much user has in hands
       result = db.execute("SELECT cash FROM users WHERE id = ?", id)
       owned = result[0]['cash']

       # check if he can buy
       if (owned >= totalPrice):
        db.execute("update users set cash = cash - ? WHERE id = ?", totalPrice, id)
        #db.execute("INSERT INTO history VALUES(?, ?, ?, ?, ?, ?, ?)", id, username[0]["username"], stock["name"], symbol, shares, stock["price"], totalPrice)
        # setar primary key em stockSymbol
        #db.execute("INSERT INTO owned VALUES(?, ?, ?, ?, ?, ?, ?) ON CONFLICT(stockSymbol) DO UPDATE SET stockQty = stockQty + ?", id, username[0]["username"], stock["name"], symbol, shares, stock["price"], totalPrice, shares)
        #db.execute("INSERT INTO history VALUES(?, ?, ?, ? ,?, ?, ?, ?,  DateTime('now'))", id, username[0]["username"], stock["name"], symbol, shares, stock["price"], totalPrice, "Buy")

        db.execute("INSERT INTO history VALUES(?, ?, ?, ? ,?, ?, ?,  DateTime('now'))", id, username[0]["username"], stock["name"], symbol, shares, stock["price"], "Buy")
        return redirect("/")

       else:
        return apology("User cannot afford that amount of shares.", 403)




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

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
            return apology("Symbol not founded", 403)

        return render_template("quoted.html", results=results)





@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

         if not request.form.get("username"):
            return apology("must provide username", 403)

         elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide a valid password", 403)

         username = request.form.get("username")
         password = request.form.get("password")
         confirmation = request.form.get("confirmation")


          #check if already exists username
         usercheck = []
         usercheck = db.execute("SELECT username from users WHERE username = ?",username)
         if len(usercheck) == 1:
            if username == usercheck[0]['username']:
                return apology("User already registered", 403)


        # Testar Registro com mesmo Usuario

         if password != confirmation:
            return apology("Passwords do not match !", 403)

         passwordHash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
         db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, passwordHash)
         return redirect("/login")


    #return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        id = session["user_id"]
        symbols = db.execute("SELECT stockSymbol from history where user_id = ? GROUP BY stockSymbol", id)
        return render_template("sell.html", symbols=symbols)
    else:
        id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")





        # Validate Symbol
        if not symbol:
            return apology("Must provide an symbol !", 403)

        if not shares:
            return apology("Must provide a share !", 403)

        #int(shares)
        stock = lookup(symbol)
        if not stock:
            return apology("Symbol not valid", 403)

        # Validate shares
        if int(shares) <= 0:
            return apology("Share it's not a positive integer", 403)

        # Check if user has that amount of shares
        ownedShares = db.execute("SELECT sum(stockQty) as stockQty FROM history where user_id = ? AND stockSymbol = ?", id, symbol)

        if int(shares) <= ownedShares[0]['stockQty']:
            # get username
            username = db.execute("SELECT username FROM users where id = ?",id)

            # get the total price
            totalPrice = float(stock['price']) * float(shares)

            # get the symbol value to return to user
            value = db.execute("SELECT price from history where user_id = ? AND stockSymbol = ?", id , symbol)

            # the value that wil  add to the user account
            returnValue = int(value[0]['price']) * shares

            # update cash from user
            db.execute("UPDATE users set cash = cash + ? WHERE id = ?", totalPrice, id)

            # decrease stock quantity
            db.execute("INSERT INTO history VALUES(?, ?, ?, ? ,?, ?, ?, DateTime('now'))", id, username[0]["username"], stock["name"], symbol, -int(shares), stock["price"], "Sell")
            #db.execute("UPDATE owned set stockQty = stockQty - ? WHERE user_id = ? AND stockSymbol = ?", shares, id, symbol)
        else:
            return apology("User doenst have that amount of shares to sell.", 403)


    return apology("TODO")
