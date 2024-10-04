# Sample database
Sample_db = {
    "1": {
        "Name": "Tom",
        "Account": "001",
        "Balance": 1000
    },
    "2": {
        "Name": "Samuel",
        "Account": "002",
        "Balance": 1000
    },
    "3": {
        "Name": "Trevor",
        "Account": "003",
        "Balance": 1000
    }
}

def get_user_details(name):
    normalized_name = name.lower()

    for details in Sample_db.values():
        if details["Name"].lower() == normalized_name:
            return details

    return "Invalid"

def deposit(account, amount_deposited):
    for details in Sample_db.values():
        if details["Account"] == account:
            details["Balance"] += amount_deposited
            return f"Deposited {amount_deposited}. New balance: {details['Balance']}"
    return "Account not found"

def withdraw(account, withdrawal_amount):
    for details in Sample_db.values():
        if details["Account"] == account:
            # Check if the balance is less than 300
            if details["Balance"] < 300:
                return "Insufficient funds"
            # Check if there are enough funds for the withdrawal
            if details["Balance"] >= withdrawal_amount:
                details["Balance"] -= withdrawal_amount
                return f"Withdrew {withdrawal_amount}. New balance: {details['Balance']}"
            else:
                return "Insufficient funds"
    return "Account not found"

# Example usage
user_input = input("Enter a name: ")
user_details = get_user_details(user_input)

if user_details == "Invalid":
    print(user_details)
else:
    print(f"Name: {user_details['Name']}")
    print(f"Account: {user_details['Account']}")
    print(f"Balance: {user_details['Balance']}")

    action = input("Would you like to deposit or withdraw?: ").lower()
    amount = float(input("Enter the amount: "))

    if action == 'deposit':
        print(deposit(user_details["Account"], amount))
    elif action == 'withdraw':
        print(withdraw(user_details["Account"], amount))
    else:
        print("Invalid action")
