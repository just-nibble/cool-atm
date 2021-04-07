from datetime import datetime
from random import randint
import json
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

session = True
logged_in = False

data = {}
data["people"] = []
money = {}
money["people"] = []


def account_number_generation():
    account = randint(0000000000, 1111111111)
    return (account)


def register():
    first_name = input("enter name: ")
    last_name = input("enter last name: ")
    password = input("enter password: ")
    full_name = first_name + " " + last_name
    balance = 0.0
    account_number = account_number_generation()
    details = {
        "name": full_name,
        account_number: "account_number",
        password: "password",
    }
    savings = {
        "amount": balance
    }
    money["people"].append(savings)
    data["people"].append(details)

    with open('money.json', 'a') as outfile:
        json.dump(money, outfile)

    with open('storage.json', 'a') as outfile:
        json.dump(data, outfile)
    print("Your account number is: ", account_number)


def login(logged_in):
    account = input("Enter account number: ")
    password = input("Enter password: ")
    with open('storage.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            if p[account] == "account_number" and p[password] == "password":
                print("welcome")
                logged_in = True
            else:
                print('invalid login credentials')
    return logged_in


def withdraw():

    with open('money.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            balance = p["amount"]
            print("Your balance is: ", balance)

    amount = float(input("Enter Amount to withdraw: \n"))
    balance = balance - amount
    print("Take your cash\n")
    savings = {
        "amount": balance
    }
    money["people"].append(savings)

    with open('money.json', 'w') as outfile:
        json.dump(money, outfile)

    print("Your balance is: ", balance)
    return balance


def deposit():

    with open('money.json', 'r') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            balance = p["amount"]
            print("Your balance is: ", balance)

    amount = float(input("Enter Amount to deposit: \n"))
    print(amount)
    balance = balance + amount
    savings = {
        "amount": balance
    }
    print(savings)
    money["people"].append(savings)
    print(money)

    with open('money.json', 'w') as outfile:
        json.dump(money, outfile)

    print("Your balance is: ", balance)
    return balance


while session:
    try:
        print(current_time)
        user_input = input(
            "1. Register\n2. Login\n3. Withdrawal\n4. Deposit\n5. Complaint\n6. Exit\n..."
        )
        option = float(user_input)
        if option == 1:
            register()
        if option == 2:
            login()

        if option == 3:
            withdraw()

        if option == 4:
            deposit()

        if option == 5:
            complaint = input("What issue will you like to report?\n..")
            print("Thank you for contacting us")
            input("Would you like to make another transaction?").lower()
            if input == "no":
                print("Thank you for banking with us")
                session = False

        if option == 6:
            print("Thank you for banking with us")
            session = False

    except Exception:
        print("Invalid input")
