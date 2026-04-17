class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn")
        else:
            print("Not enough balance")

    def show_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


def main():
    acc = BankAccount("Jahongir", 1000)

    acc.show_balance()
    acc.deposit(500)
    acc.withdraw(300)
    acc.withdraw(2000)

    acc.show_balance()


main()
