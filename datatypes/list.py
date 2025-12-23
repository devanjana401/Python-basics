# ordered,mutable

list1 = ["apple",1,2,3,"banana",4,5,6]
list2 = [7,8,"orange"]

list3 = []    #empty list
list4 = list()    #empty list using list(keyword in python)
list5 = list((1,2,3)) #convert tuple into list

print("list5:",list5)  
print("list1[0]:",list1[0])  #first element
print("list1[-1]:",list1[-1])  #last element
print("list1[:4]:",list1[:4])    #first 4 element
print("list1[2:]:",list1[2:])    #from index 2 to till end
print("list1[2:5]",list1[2:5])   #from index 2 to 4
print("list1[::-1]:",list1[::-1])  #reverse order
print("list1+list2:",list1+list2)  #concatenation
list1[1] = "watermelon"            #reassignment
print("After reassigning:",list1)
