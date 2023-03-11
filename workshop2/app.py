from banking_pkg import account
global balance


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
# make first letter always capitalized later or lowercase here?
name = input("Enter name to register: ")
# data type should be int for pin here, inputs are by default str
pin = int(input("Enter Pin: "))
balance = 0  # global var, will need to be declared to change inside local function
print(f"{name} has been registered with a starting balance of ${balance}")

while True:
    print("          === Automated Teller Machine ===          ", "\n", "LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = int(input("Enter Pin: "))
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = int(input("Choose an option: "))
    if option == 1:
        account.show_balance(balance)

    elif option == 2:
        balance = account.deposit(balance)
        account.show_balance(balance)

    elif option == 3:
        balance = account.withdraw(balance)
        account.show_balance(balance)

    elif option == 4:
        account.logout(name)
        break
