from datetime import datetime

class Transaction:
    def __init__(self, amount, trans_type):
        self.amount = amount
        self.trans_type = trans_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save(self):
        with open("transactions.txt", "a") as file:
            file.write(f"{self.date} - {self.trans_type} - ${self.amount}\n")

    def summary(self):
        print(f"{self.date} - {self.trans_type} - ${self.amount}")

t1 = Transaction(500, "Deposit")
t1.save()
t1.summary()

t2 = Transaction(150, "Withdraw")
t2.save()
t2.summary()

t3 = Transaction(300, "Deposit")
t3.save()
t3.summary()

print("\nTransaction History:")
with open("transactions.txt", "r") as file:
    for line in file:
        print(line.strip())