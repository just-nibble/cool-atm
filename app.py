from datetime import datetime
from packages.base import register, login, withdraw, deposit
import json
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

session = True


while session:
    try:
        print(current_time)
        user_input = input(
            "1. Register\n2. Login\n3. Withdrawal\n4. Deposit\n5. Complaint\n6. Exit\n..."
        )
        option = float(user_input)
        if option == 1:
            print("time is: ", current_time)
            register()
        if option == 2:
            print("time is: ", current_time)
            login()

        if option == 3:
            print("time is: ", current_time)
            withdraw()

        if option == 4:
            print("time is: ", current_time)
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
