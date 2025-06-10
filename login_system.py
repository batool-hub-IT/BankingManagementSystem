import os
import getpass
from datetime import datetime

class AlertSystem:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone
    def send_email(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time}] Email to {self.email}: {message}")
    def send_whatsapp(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time}] WhatsApp to {self.phone}: {message}")
    def deposit(self, amount):
        print(f"Depositing ${amount}")
        self.send_email(f"Deposit of ${amount} is successful.")
    def withdraw(self, amount):
        print(f"Withdrawing ${amount}")
        if amount > 500:
            self.send_whatsapp("Your balance is low.")
        self.send_email(f"Withdrawal of ${amount} is done.")
    def transfer(self, amount, to_email):
        print(f"Transferring ${amount} to {to_email}")
        self.send_email(f"You sent ${amount} to {to_email}")
        self.send_whatsapp("Transfer completed.")

class Transaction:
    def __init__(self, user, amount, type_):
        self.user = user
        self.amount = amount
        self.type = type_
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def __str__(self):
        return f"{self.date} | {self.type.upper()} | User: {self.user} | Amount: ${self.amount}"

class BankSystem:
    def __init__(self):
        self.users = {}
        self.balances = {}
        self.transactions = []
    def add_transaction(self, username, amount, type_):
        tx = Transaction(username, amount, type_)
        self.transactions.append(tx)
        if type_ == 'deposit':
            self.balances[username] += amount
        elif type_ == 'withdraw':
            self.balances[username] -= amount
        self.save_transaction(tx)
    def delete_transaction(self, index):
        if 0 <= index < len(self.transactions):
            tx = self.transactions.pop(index)
            if tx.type == 'deposit':
                self.balances[tx.user] -= tx.amount
            elif tx.type == 'withdraw':
                self.balances[tx.user] += tx.amount
            print("Transaction deleted.")
        else:
            print("Invalid index.")
    def get_total_amounts(self):
        total_deposit = sum(t.amount for t in self.transactions if t.type == 'deposit')
        total_withdraw = sum(t.amount for t in self.transactions if t.type == 'withdraw')
        return total_deposit, total_withdraw
    def get_user_balance(self, username):
        return self.balances.get(username, 0.0)
    def save_transaction(self, tx):
        with open("transactions.txt", "a") as file:
            file.write(f"{tx}\n")

class AdminPortal:
    def __init__(self, bank_system):
        self.bank_system = bank_system
    def menu(self):
        while True:
            print("\n--- Admin Portal ---")
            print("1. View All Transactions")
            print("2. Delete Transaction")
            print("3. Check Total Deposited/Withdrawn")
            print("4. Exit Admin Portal")
            choice = input("Choose an option: ").strip()
            if choice == '1':
                self.view_transactions()
            elif choice == '2':
                self.delete_transaction()
            elif choice == '3':
                self.check_totals()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
    def view_transactions(self):
        if not self.bank_system.transactions:
            print("No transactions found.")
            return
        for i, tx in enumerate(self.bank_system.transactions):
            print(f"{i}: {tx}")
    def delete_transaction(self):
        try:
            index = int(input("Enter transaction index to delete: "))
            self.bank_system.delete_transaction(index)
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    def check_totals(self):
        deposit, withdraw = self.bank_system.get_total_amounts()
        print(f"Total Deposited: ${deposit}")
        print(f"Total Withdrawn: ${withdraw}")

class UserPortal:
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.username = None
    def menu(self):
        while True:
            print(f"\n--- Welcome, {self.username} ---")
            print("1. View Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Receive Alert (Simulated)")
            print("5. Logout")
            choice = input("Choose an option: ").strip()
            if choice == '1':
                self.view_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.alert()
            elif choice == '5':
                print("Logging out.")
                break
            else:
                print("Invalid choice.")
    def view_balance(self):
        balance = self.bank_system.get_user_balance(self.username)
        print(f"Current Balance: ${balance}")
    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.bank_system.add_transaction(self.username, amount, 'deposit')
                print(f"Deposited ${amount}.")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            current_balance = self.bank_system.get_user_balance(self.username)
            if 0 < amount <= current_balance:
                self.bank_system.add_transaction(self.username, amount, 'withdraw')
                print(f"Withdrew ${amount}.")
            else:
                print("Insufficient balance or invalid amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    def alert(self):
        alert = AlertSystem("user@example.com", "+123456789")
        alert.send_email("Simulated login alert.")
        alert.send_whatsapp("This is a test WhatsApp alert.")

class LoginSystem:
    USER_FILE = 'users.txt'
    ADMIN_FILE = 'admin.txt'

    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.ensure_default_admin()

    def ensure_default_admin(self):
        admin_file = LoginSystem.ADMIN_FILE
        default_admin = "admin,admin123"

        if not os.path.exists(admin_file):
            with open(admin_file, 'w') as f:
                f.write(default_admin + "\n")
        else:
            with open(admin_file, 'r') as f:
                lines = [line.strip() for line in f.readlines()]
            if default_admin not in lines:
                with open(admin_file, 'a') as f:
                    f.write(default_admin + "\n")

    def load_credentials(self, file_path):
        creds = {}
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) >= 2:
                        username = parts[0].strip()
                        password = parts[1].strip()
                        creds[username] = password
        return creds

    def save_credentials(self, file_path, username, password):
        with open(file_path, 'a') as f:
            f.write(f"{username},{password}\n")

    def admin_login(self):
        print("\n--- Admin Login ---")
        username = input("Admin Username: ").strip()
        password = getpass.getpass("Password: ").strip()

        admins = self.load_credentials(self.ADMIN_FILE)

        if username in admins:
            if admins[username] == password:
                print("Admin login successful.")
                AdminPortal(self.bank_system).menu()
            else:
                print("Incorrect password.")
        else:
            print("Admin not found.")

    def user_signup(self):
        print("\n--- User Sign-Up ---")
        username = input("Choose a Username: ").strip()
        users = self.load_credentials(self.USER_FILE)
        if username in users:
            print("Username already exists.")
            return
        password = getpass.getpass("Choose a Password: ").strip()
        confirm = getpass.getpass("Confirm Password: ").strip()
        if password != confirm:
            print("Passwords do not match.")
            return
        self.save_credentials(self.USER_FILE, username, password)
        self.bank_system.users[username] = password
        self.bank_system.balances[username] = 0.0
        print("Sign-up successful. You may now log in.")

    def user_login(self):
        print("\n--- User Login ---")
        username = input("Username: ").strip()
        password = getpass.getpass("Password: ").strip()
        users = self.load_credentials(self.USER_FILE)
        if users.get(username) == password:
            self.bank_system.users[username] = password
            if username not in self.bank_system.balances:
                self.bank_system.balances[username] = 0.0
            print("Login successful.")
            portal = UserPortal(self.bank_system)
            portal.username = username
            portal.menu()
        else:
            print("Invalid user credentials.")

class MainMenu:
    def __init__(self):
        self.bank_system = BankSystem()
        self.login_system = LoginSystem(self.bank_system)
    def show(self):
        while True:
            print("\n=== Main Menu ===")
            print("1. Admin Login")
            print("2. User Login")
            print("3. User Sign-Up")
            print("4. Exit")
            choice = input("Select an option: ").strip()
            if choice == '1':
                self.login_system.admin_login()
            elif choice == '2':
                self.login_system.user_login()
            elif choice == '3':
                self.login_system.user_signup()
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    MainMenu().show()