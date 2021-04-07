import sqlite3
from random import randint

db = sqlite3.connect('data.sqlite3')


def account_number_generation():
    account = randint(0000000000, 1111111111)
    return (account)


def register():
    uuid = str(randint(000, 111))
    first_name = input("enter name: ")
    last_name = input("enter last name: ")
    account_number = str(account_number_generation())
    password = input("enter password: ")
    amount = 0.0
    balance = str(amount)

    peopleValues = (uuid, first_name, last_name, account_number, password)
    accountValues = (account_number, balance)
    c = db.cursor()
    c.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?)", peopleValues)
    c.execute("INSERT INTO account VALUES(?, ?)", accountValues)
    db.commit()
    with open('account_number.txt', 'a') as f:
        f.write(account_number)


def login():
    account = input("Enter account number: ")
    password = input("Enter password: ")
    try:
        for row in db.execute("SELECT * FROM user WHERE account_number = ?", (account,)):
            if row[4] == password:
                print("Login Successful")
                logged_in = True
            else:
                print("invalid Password")
        return logged_in
    except Exception:
        print("Account number not found")


def withdraw():
    account = input("Enter account number: ")
    while True:
        try:
            for row in db.execute("SELECT * FROM account WHERE owner = ?", (account,)):
                balance = row[1]
                amount = float(balance)
                print("Your balance is: ", balance)

            amount_to_withdraw = float(input("Enter Amount to withdraw: \n"))
            balance = balance - amount_to_withdraw
            print("Take your cash\n")
            c = db.cursor()
            c.executemany('insert into account values (?)', balance)

            print("Your balance is: ", balance)
            return balance
        except Exception:
            print("Wrong account")


def deposit():
    account = input("Enter account number: ")
    while True:
        try:
            for row in db.execute("SELECT * FROM account WHERE owner = ?", (account,)):
                balance = row[1]
                amount = float(balance)
                print("Your balance is: ", balance)

            amount_to_deposit = float(input("Enter Amount to deposit: \n"))
            balance = balance + amount_to_deposit
            c = db.cursor()
            c.executemany('insert into account values (?)', balance)

            print("Your balance is: ", balance)
            return balance
        except Exception:
            print("Wrong account")
