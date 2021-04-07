from datetime import datetime
from random import randint

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

session = True
current_balance = 0.0


def account_number_generation():
    account = randint(0000000000, 1111111111)
    return("your account number is " account)


def register():
    first_name = input("enter name: ")
    last_name = input("enter last name: ")
    full_name = first_name + last_name
    account_number = account_number_generation()
    f = open("storage.txt", "a")
    f.write("{\n"account_number "\n"full_name "}\n")
    f.close()


def login():
    match = input("Enter account number: ")
    file = open('file.txt')
    for line in file:
        line.strip().split('/n')
        if line.startswith(match):
            print line
    file.close()


while session:
    try:
        print(current_time)
        user_input = input(
            "1. Register\n2. Login\n3. Withdrawal\n4. Deposit\n5. Complaint\n6. Exit\n..."
        )
        option = float(user_input)

        if option == 3:
            withdrawal = input("How much would you like to withdraw\n..")
            print("Take your cash\n")
            input("Would you like to make another transaction?").lower()
            if input == "no":
                print("Thank you for banking with us")
                session = False

        if option == 4:
            withdrawal = input("How much would you like to deposit\n..")
            added_amout = float(withdrawal)
            current_balance = current_balance + added_amout
            print(current_balance)
            input("Would you like to make another transaction?").lower()
            if input == "no":
                print("Thank you for banking with us")
                session = False

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
