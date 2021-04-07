from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

session = True
current_balance = 0.0

while session:
    try:
        print(current_time)
        user_input = input(
            "1. Withdrawal\n2. Deposit\n3. Complaint\n4. Exit\n..."
        )
        option = float(user_input)

        if option == 1:
            withdrawal = input("How much would you like to withdraw\n..")
            print("Take your cash\n")
            input("Would you like to make another transaction?").lower()
            if input == "no":
                print("Thank you for banking with us")
                session = False

        if option == 2:
            withdrawal = input("How much would you like to deposit\n..")
            added_amout = float(withdrawal)
            current_balance = current_balance + added_amout
            print(current_balance)
            input("Would you like to make another transaction?").lower()
            if input == "no":
                print("Thank you for banking with us")
                session = False

        if option == 3:
            complaint = input("What issue will you like to report?\n..")
            print("Thank you for contacting us")
            input("Would you like to make another transaction?").lower()
            if input == "no":
                print("Thank you for banking with us")
                session = False

        if option == 4:
            print("Thank you for banking with us")
            session = False

    except Exception:
        print("Invalid input")
