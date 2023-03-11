def show_balance(balance):
    print(f"Your current balance is: ${balance}")
    # assume float value for balance


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("invalid withdrawal amount")
    elif amount < balance:
        return balance - amount
    else:
        print("Invalid input, please try again.")
        withdraw(balance)


def logout(name):
    print("Goodbye ", name, "!")
