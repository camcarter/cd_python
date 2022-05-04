class BankAccount:
    accounts = []
    def __init__(self, int_rate=0.03, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Bank Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(1000).deposit(1500).deposit(2000).withdraw(500).yield_interest().display_account_info()
account2.deposit(150).deposit(150).withdraw(60).withdraw(60).withdraw(80).withdraw(20).yield_interest().display_account_info()