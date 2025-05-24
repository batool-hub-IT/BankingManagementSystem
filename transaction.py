# order.py

def show_menu():
    print("\n-------- Simple Bank Menu --------")
    print("1. Create Account")
    print("2. View Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. View Last 5 Transactions")
    print("7. View Full Payment History")
    print("8. Exit")

def create_account():
    print("Account created successfully!")
    return {"balance": 0.0, "transactions": []}

def is_number(s):
    dot_count = 0
    for ch in s:
        if ch == '.':
            dot_count += 1
        elif ch < '0' or ch > '9':
            return False
    return dot_count <= 1 and s != '' and s != '.'

def view_balance(account):
    print("Your current balance is: $", round(account["balance"], 2))

def deposit_money(account):
    amount_input = input("Enter amount to deposit: ")
    if is_number(amount_input):
        amount = float(amount_input)
        if amount > 0:
            account["balance"] += amount
            account["transactions"].append(f"Deposited ${round(amount, 2)}")
            print("Deposit successful!")
        else:
            print("Amount must be positive.")
    else:
        print("Invalid input. Please enter a valid number.")

def withdraw_money(account):
    amount_input = input("Enter amount to withdraw: ")
    if is_number(amount_input):
        amount = float(amount_input)
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > account["balance"]:
            print("Insufficient balance.")
        else:
            account["balance"] -= amount
            account["transactions"].append(f"Withdrew ${round(amount, 2)}")
            print("Withdrawal successful!")
    else:
        print("Invalid input. Please enter a valid number.")

def transfer_money(account):
    print("Transfer feature not implemented yet.")

def view_last_5_transactions(account):
    print("\n--- Last 5 Transactions ---")
    for t in account["transactions"][-5:]:
        print(t)

def view_full_history(account):
    print("\n--- Full Payment History ---")
    for t in account["transactions"]:
        print(t)


