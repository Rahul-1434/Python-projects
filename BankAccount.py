class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return f"deposited {amount} to your account"
    def withdraw(self,amount):
        if self.balance<amount:
            return "Not enough balance!!"
        else:
            self.balance-=amount
            return "successfully withdrew"
    def __str__(self):
        return f"Acount Holder Name:{self.name}\nBalance:{self.balance}"
obj=BankAccount('rahul',500)
print(obj)
print(obj.deposit(200))
print(obj.withdraw(300))
print(obj.withdraw(1000))
print(obj)
