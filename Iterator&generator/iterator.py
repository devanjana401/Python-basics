# Itearor - an object that allows you to access items one by one
# two methods :-
#   ----  __iter__()  -- creating iterator
#   ----  __next__()  -- accessing elements one by one
# used to save memory,process large data,accessing sequence without using indexes
# Iterator = remembers state + gives next value until stopped

# example 1
numbers = [10,20,30]
it = iter(numbers)        # creating iterator
print(next(it))
print(next(it))
print(next(it))

# example 2
class count:
    def __init__(self,limit):       # __init__ ----> used to intialize constructor
        self.limit = limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration     # raise - intentionally raising an error
c = count(5)
for i in c:
    print(i)
