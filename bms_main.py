import getpass

class Transaction:
    def __init__(self, user, amount, type_):
        self.user = user
        self.amount = amount
        self.type = type_

    def __str__(self):
        return f"{self.type.upper()} | User: {self.user} | Amount: ${self.amount}"

class BankSystem:
    def __init__(self):
        self.users = {'user1': 'pass123'}
        self.balances = {'user1': 0.0}
        self.transactions = []

    def add_transaction(self, username, amount, type_):
        self.transactions.append(Transaction(username, amount, type_))
        if type_ == 'deposit':
            self.balances[username] += amount
        elif type_ == 'withdraw':
            self.balances[username] -= amount

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

    def login(self):
        print("\n--- User Login ---")
        uname = input("Username: ").strip()
        pword = getpass.getpass("Password: ").strip()

        if self.bank_system.users.get(uname) == pword:
            self.username = uname
            print("Login successful.")
            self.menu()
        else:
            print("Invalid credentials.")

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
        print("🔔 Alert: This is a simulated notification. Your account is safe!")

class MainMenu:
    def __init__(self):
        self.bank_system = BankSystem()

    def show(self):
        while True:
            print("\n=== Main Menu ===")
            print("1. Admin Portal")
            print("2. User Portal")
            print("3. Exit")

            choice = input("Select an option: ").strip()
            if choice == '1':
                AdminPortal(self.bank_system).menu()
            elif choice == '2':
                UserPortal(self.bank_system).login()
            elif choice == '3':
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    MainMenu().show()
1