# collection of unique items(no duplicates),unordered,mutable

set1 = {1,2,3,4,5}
set2 = {"apple","banan","cherry"}
set3 = set([1,2,2,3,4,5])   # duplicates removed
print("set3:",set3)
# adding,removing
set1.add(6)
print("After add:",set1)
set1.remove(3)     # removes element,error if not present
print("After remove:",set1)
set1.discard(10)   # no error if eleemnt not present

# set operations
a = {1,2,3,4}
b = {3,4,5,6}
print("Union:",a|b)           #{1,2,3,4,5,6}
print("Intersection:",a&b)    #{3,4}
print("Difference:",a-b)      #{1,2}  -- when it as b-a o/p is {5,6}
print("Symmetric diff:",a^b)  #{1,2,5,6}