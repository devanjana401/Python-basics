# example 1

class Product:
    
    discount = 5  # Static variable (shared by all)
    total_product=0
    
    def __init__(self, name, price):
        self.name = name     # Instance variable
        self.price = price   # Instance variable
        Product.total_product+=1

    def display(self):
        print(f"Name: {self.name}, Price: {self.price}, Discount: {Product.discount}%")

    @classmethod
    def change_discount(cls,new_discount):
        cls.discount=new_discount

product1 = Product("Pen", 10)
print("total products :",Product.total_product)
product2 = Product("Book", 50)
print("total products :",Product.total_product)

product1.display()
product2.display()

product1.name="Pencil"# changing instance variable 
product1.display()

# # Changing static variable affects all objects
Product.discount = 10
product1.display()
product2.display()
Product.change_discount(20)
product2.display()


# example 2
class BankAccount:
    bank_name="State Bank Of India" # static(class) vriable
    
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
        print(f"balance of {self.account_holder} is : {self.balance} , Bank : {BankAccount.bank_name}") 
    # class method
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
        print(f"Bank name changed to : {cls.bank_name}")
acc1=BankAccount("Anu",1000)
acc2=BankAccount("Ajay",7000)
acc1.deposit(2000)
acc2.withdraw(500)
acc1.display_balance()
acc2.display_balance()
# Change class variable using class method
BankAccount.change_bank_name("HDFC Bank")
print("\n after changing bank")
acc1.display_balance()
acc2.display_balance()