# Create a class BankAccount that has:
# Attributes: account_holder, balance
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
class BankAccount:
    
    def __init__(self,account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"new balance of {self.account_holder} is : {self.balance}")
        
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"new balance of {self.account_holder} is : {self.balance}")
        else:
            print("Insufficient Balance!")
            
        
    def display_balance(self):
        print(f"balance of {self.account_holder} is : {self.balance}")        
acc=BankAccount("Anu",1000)
acc.deposit(2000)
acc.withdraw(500)