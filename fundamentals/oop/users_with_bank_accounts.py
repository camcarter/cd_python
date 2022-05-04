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
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.03, balance=0)

def deposit(self, amount):
    print("[ + ] - ", end='')
    self.account.deposit(amount)
    print(f"Deposited ${amount} into {self.username}'s account")
    return self

def withdrawal(self, amount):
    print("[ - ] - ", end ='')
    self.account.withdrawal(amount)
    print(f"Withdrew ${amount} from {self.username}'s account")
    return self

def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self

cam = User("Cam Carter", "cartercam59@gmail.com")
ethan = User("Ethan Carter", "ethancarter57@gmail.com")