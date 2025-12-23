# ordered,immutable

tuple1 = ("apple",1,2,3,"banana",4,5,6)
tuple2 = (7,8,"orange")

tuple3 = ()    #empty list
tuple4 = tuple()    #empty list using tuple(keyword in python)
tuple5 = tuple([1,2,3]) #convert list into tuple

print("tuple5:",tuple5)  
print("tuple1[0]:",tuple1[0])  #first element
print("tuple1[-1]:",tuple1[-1])  #last element
print("tuple1[:4]:",tuple1[:4])    #first 4 element
print("tuple1[2:]:",tuple1[2:])    #from index 2 to till end
print("tuple1[2:5]",tuple1[2:5])   #from index 2 to 4
print("tuple1[::-1]:",tuple1[::-1])  #reverse order
print("tuple1+tuple2:",tuple1+tuple2)  #concatenation
