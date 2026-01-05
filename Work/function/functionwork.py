#1. simple function

# example1
def greet_customer():
    print("Welcome to our shop! Have a great day 😊")

# example2
def display_menu():
    print("Menu:")
    print("1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Coffee")

greet_customer()
display_menu()


#2. function with return statement

# example1
def convert_to_usd(amount_in_inr):
    return amount_in_inr / 83

# example2
def final_price(price, discount):
    return price - (price * discount / 100)

# example3
def delivery_charge(distance):
    if distance <= 5:
        return 30
    elif distance <= 10:
        return 50
    else:
        return 100

print("USD:", convert_to_usd(830))
print("Final Price:", final_price(1000, 10))
print("Delivery Charge:", delivery_charge(12))


#3. default parameter

# example1
def book_ticket(name, seat="General"):
    print(f"Ticket booked for {name} | Seat: {seat}")

# example2
def send_email(to, subject="No Subject", message="Empty"):
    print("To:", to)
    print("Subject:", subject)
    print("Message:", message)

book_ticket("Anjana")
book_ticket("Anjana", "Sleeper")
send_email("test@gmail.com")
send_email("test@gmail.com", "Hello", "Welcome!")


#4. keyword arguments

# example1
def create_account(name, age, balance):
    print(name, age, balance)

create_account(balance=5000, name="Anjana", age=21)

# example2
def movie_ticket(movie, seat, price):
    print("Movie:", movie)
    print("Seat:", seat)
    print("Price:", price)

movie_ticket(price=250, movie="Interstellar", seat="A10")


#5. variable length arguments (*args)

# example1
def calculate_total(*prices):
    total = 0
    for p in prices:
        total += p
    return total

# example2
def find_average_score(*scores):
    total = 0
    for s in scores:
        total += s
    return total / len(scores)

# example3
def combine_names(*names):
    full_name = ""
    for n in names:
        full_name += n + " "
    return full_name.strip()

print("Total Bill:", calculate_total(100, 200, 50))
print("Average Score:", find_average_score(80, 90, 70))
print("Full Name:", combine_names("Anjana", "Sasi"))


#6. variable length keyword arguments (**kwargs)

# example1
def student_profile(**details):
    for key, value in details.items():
        print(key, ":", value)

# example2
def place_order(**items):
    total = 0
    for item, price in items.items():
        print(item, "Rs.", price)
        total += price
    print("Total =", total)

# example3
def employee_record(**info):
    for key, value in info.items():
        print(key, ":", value)

student_profile(name="Anjana", age=21, city="TVM")
place_order(pizza=250, burger=120, coffee=80)
employee_record(id=101, name="Rahul", salary=30000, dept="IT")


# advanced 

# example1
def atm_withdraw(balance, amount, limit=20000):
    if amount > limit:
        return "Limit exceeded"
    elif amount > balance:
        return "Insufficient balance"
    else:
        return balance - amount

print("Balance:", atm_withdraw(30000, 5000))

# example2
def shopping_cart(*items, **discounts):
    total = sum(items)
    discount_total = sum(discounts.values())
    return total - discount_total

print("Final Amount:", shopping_cart(100, 200, 300, d1=50, d2=30))

# example3
def library_member(name, *books, **details):
    print("Member Name:", name)
    print("Books:", books)
    print("Details:")
    for key, value in details.items():
        print(key, ":", value)

library_member(
    "Anjana",
    "Python", "AI",
    membership="Premium",
    expiry="2026"
)
