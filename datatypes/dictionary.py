# key-value pairs,unordered,mutable

student = {"name":"Anjana","age":"23","grade":"A"}

print(student["name"])     #Anjana
student["age"] = 21        #update
student["course"] ="ECE"   #add
print(student)

student2 = {
    "name":"Anju",
    "age":"22",
    "course":"CS"
}
print(student2["name"])
print(student2.get("age"))  # 22
print(student2.keys())      # dict_keys(['name','age','course'])
print(student2.values())    # dict_values(['Anju','22','CS'])
