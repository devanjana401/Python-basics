import random

print(random.randint(1, 10))  # random number between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))
print(random.random())#Generates a random float between 0.0 and 1.0
print(random.uniform(1, 10))#Returns a random float between a and b
print(random.randrange(0, 10, 2))  # even numbers between 0 and 9
colors = ["red", "green", "blue"]
print(random.choices(colors, k=5))#Selects multiple random elements (with replacement).
print("Rolling the dice...")
dice = random.randint(1, 6)
print("You got:", dice)