from cs50 import SQL

db = SQL("sqlite:///finance.db")

username = []

admin = "admin"

username = db.execute("SELECT username from users where username = ?", admin)

print(username[0]['username'])
print(len(username))