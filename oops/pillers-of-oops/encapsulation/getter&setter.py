# Accessing Private Data Using Methods (Getters and Setters)


# example 1
# class Student: 
#     def __init__(self, marks): 
#         self.__marks = marks 
 
#     def get_marks(self): 
#         return self.__marks 

#     def set_marks(self, new_marks): 
#         if new_marks >= 0 and new_marks <= 100: 
#             self.__marks = new_marks 
#         else: 
#             print("Invalid marks") 
# s = Student(80) 
 
# print(s.get_marks())      # accessing private data 
# s.set_marks(90)           # modifying private data 
# print(s.get_marks())

# Private variable: __marks 
# get_marks() gives read access 
# set_marks() controls write access 
#  We protect marks from invalid values


# example 2
# class ATM: 
#     def __init__(self, pin): 
#         self.__pin = pin 
 
#     def get_pin(self): 
#         return "PIN is protected. Cannot show." 
 
#     def change_pin(self, old_pin, new_pin): 
#         if old_pin == self.__pin: 
#             if len(str(new_pin)) == 4: 
#                 self.__pin = new_pin 
#                 print("PIN changed successfully") 
#             else: 
#                 print("PIN must be 4 digits") 
#         else: 
#             print("Wrong old PIN") 
 
# a = ATM(1234) 
# print(a.get_pin()) 
# a.change_pin(1234, 5678) 

# PIN is private. 
# User cannot see it directly. 
# User can only change the PIN using the method change_pin(). 
# Encapsulation protects the PIN from unauthorized access.


# example 3
# bank  and atm pin
class BankAccount:
    def __init__(self, acc_holder,pin,balance=0):
        #private attributes 
        self.__acc_holder=acc_holder
        self.__pin =str(pin)
        self.__balance=float(balance)
        self.__pin_attempts=0
        self.__max_attempts=3
        self.__locked=False
        
    def __verify_pin(self, pin_input):
        if self.__locked:
            print("account is locked ")
            return
        if str(pin_input) == self.__pin:
            self.__pin_attempts=0
            return True
        else:
            self.__pin_attempts+=1
            attempts_left=self.__max_attempts-self.__pin_attempts
            if attempts_left<=0:
                self.__locked=True
                print("Incorrect PIN, account Locked..! ")
            else:
                print(f"incorrect PIN attempts left : {attempts_left}")
            return False
            
    def  check_balance(self,pin_input):
        if self.__verify_pin(pin_input):
            print(f"Available Balance : rs.{self.__balance:.2f}")
            return self.__balance
        return None

    def change_pin(self,current_pin, new_pin):
        if not (str(new_pin).isdigit() and len(str(new_pin))==4):
            print("pin must be exactly 4 digits.")
            return False
        if self.__verify_pin(current_pin):
            self.__pin=str(new_pin)
            print("pin changed successfully")
            return 
        return False

acc=BankAccount("Anu",pin=1234,balance=50000)
while True:                   
    print("\n==== ATM MENU ====")
    print("1. Check Balance")
    print("2. Change PIN")
    print("3. Exit")
    choice = input("choose (1-3): ").strip()

    if choice == '1':
        pin=input("Enter a pin : ")
        acc.check_balance(pin)
    elif choice == '2':
        c_pin=input("Enter current  pin : ")
        n_pin=input("Enter new  pin : ")
        acc.change_pin(c_pin,n_pin)
    elif choice=='3':
        print("exit....")
        break
    else:
        print("invalid choice..")