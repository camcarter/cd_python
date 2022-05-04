from unicodedata import name


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def display_balance(self):
        pass
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

armen = User("Armen", "armen@gmail.com")
noah = User("Noah", "noah@gmail.com")
cam = User("Cam", "cam@gmail.com")

armen.make_deposit(1000)
armen.make_deposit(1500)
armen.make_deposit(2000)
armen.make_withdrawal(1715)
print(armen.account_balance)

noah.make_deposit(500)
noah.make_deposit(1000)
noah.make_withdrawal(100)
noah.make_withdrawal(200)
print(noah.account_balance)

cam.make_deposit(5000)
cam.make_withdrawal(200)
cam.make_withdrawal(200)
cam.make_withdrawal(200)
print(cam.account_balance)

# BONUS TRANSFER
armen.make_withdrawal(500)
print(armen.account_balance)
armen.transfer_money(noah, 325)
print(armen.account_balance)
print(noah.account_balance)