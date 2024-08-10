# START OF PROGRAM 

initial_balance = 1000
balance = initial_balance
pin = "1234"
transaction_history = []

while True:
    print("\nTHE ATM MACHINE")
    print("1. Account Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print(f"Account Balance: ${balance}")
        else:
            print("Incorrect PIN. Please try again.")

    elif choice == "2":
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                confirmation = input(f"Confirm withdrawal of ${amount}? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    entered_pin = input("Enter your PIN to confirm the transaction: ")
                    if entered_pin == pin:
                        balance -= amount
                        transaction_history.append(f"Withdrawn: ${amount}")
                        print(f"${amount} withdrawn successfully.")
                    else:
                        print("Incorrect PIN. Transaction cancelled.")
                else:
                    print("Transaction cancelled.")
        except ValueError:
            print("Invalid Input, Please Enter A Numerical Value.")

    elif choice == "3":
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            else:
                confirmation = input(f"Confirm deposit of ${amount}? (yes/no): ").strip().lower()
                if confirmation == "yes":
                    entered_pin = input("Enter your PIN to confirm the transaction: ")
                    if entered_pin == pin:
                        balance += amount
                        transaction_history.append(f"Deposited: ${amount}")
                        print(f"${amount} deposited successfully.")
                    else:
                        print("Incorrect PIN. Transaction cancelled.")
                else:
                    print("Transaction cancelled.")
        except ValueError:
            print("Invalid Input, Please Enter A Numerical Value.")

    elif choice == "4":
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
        else:
            print("Incorrect PIN. Please try again.")

    elif choice == "5":
        print("Exiting, Thank you for you the ATM machine")
        break

    else:
        print("Invalid choice. Please try again.")








