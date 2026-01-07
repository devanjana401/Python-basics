# Original dictionary
student = {"name": "Anu", "age": 20, "grade": "A"}
print("Original dictionary:", student)
# keys(), values(), items()
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# get()
# student['name']
print("Get name:", student.get("name"))
print("Get roll with default:", student.get("roll",101))
# update()
student.update({"age":21, "city":"Kochi"})
print("After update:", student)

# pop() and popitem()
removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)
removed_item = student.popitem()
print("Removed last item:", removed_item)
print("After popitem:", student)

# setdefault()
print(student)
print(student.setdefault("grade","B"))
# student.setdefault("grade","B")
print("After setdefault:", student)
# student.setdefault("grade","A")
print(student.setdefault("grade","A"))
print("After setdefault:", student)
# copy() and clear()
student_copy = student.copy()
print("Copy:", student_copy)
student.clear()
print("After clear:", student)

