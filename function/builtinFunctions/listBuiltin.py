fruits = ["apple","banana"]
# append() -> add item at end
fruits.append("cherry")
print("append:",fruits)
# insert(index,value) -> add at specific position
fruits.insert(1,"mango")
print("insert:",fruits)
# extend(iterable) -> add multiple items
fruits.extend(["grape","orange"])
print("extend:",fruits)

fruits1 = ["apple","banana","cherry","apple"]
# remove(value) -> removes first occurence
fruits1.remove("apple")
print("remove:",fruits1)
# pop(index) -> removes item at index(default last)
fruits1.pop()
print("pop last:",fruits1)
fruits1.pop(0)
print("pop index 0:",fruits1)
# clear() -> removes all item
fruits1.clear()
print("clear:",fruits1)

