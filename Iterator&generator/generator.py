# generator - special type of iterator/simpler way to create iterator
# it is function that used yield keyword to return values one at a time
# it automatically create __iter__() and __next__() methods
# yield pauses function and returns a value

# example 1
def numbers():
    yield 1
    yield 2
    yield 3
for n in numbers():
    print(n)

# example 2
# generator for counting
def count(limit):
    i = 1
    while i <= limit:
        yield i 
        i+= 1
for n in count(5):
    print(n)

# example 3
# even numbers
def even_numbers(limit):
    for i in range(0,limit+1,2):
        yield i
for n in even_numbers(10):
    print(n)