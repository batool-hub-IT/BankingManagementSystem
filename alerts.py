from datetime import datetime
from colorama import Fore, Style, init

init()

class AlertSystem:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def send_email(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Fore.GREEN + "[" + time + "] Email to " + self.email + ": " + message)

    def send_whatsapp(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Fore.CYAN + "[" + time + "] WhatsApp to " + self.phone + ": " + message)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.send_email("Deposit of $" + str(amount) + " is successful.")

    def withdraw(self, amount):
        print("Withdrawing $" + str(amount))
        if amount > 500:
            self.send_whatsapp("Your balance is low.")
        self.send_email("Withdrawal of $" + str(amount) + " is done.")

    def transfer(self, amount, to_email):
        print("Transferring $" + str(amount) + " to " + to_email)
        self.send_email("You sent $" + str(amount) + " to " + to_email)
        self.send_whatsapp("Transfer completed.")

if __name__ == "__main__":
    alert = AlertSystem("user@example.com", "+123456789")
    alert.deposit(1000)
    alert.withdraw(600)
    alert.transfer(250, "friend@example.com")
