#Student Management System using Class and OOP
class Student :
    #static variable to store all student objects
    student_list=[]
    def __init__(self,roll_no,name,age,course):
        self.roll_no=roll_no
        self.name=name
        self.age=age
        self.course=course
        
    def dispaly(self):
        print(f"Roll No:{self.roll_no}, Name:{self.name}, Age:{self.age}, Course:{self.course} ")
    @classmethod
    def add_student(cls):
        roll=input("Enter Roll No: ")
        name=input("Enter Name: ")
        age=input("Enter Age: ")
        course = input("Enter Course: ")
        s=Student(roll,name,age,course)
        cls.student_list.append(s)
        print("\n student added succesfully")
    @classmethod
    def dispaly_all(cls):
        if len(cls.student_list)==0:
            print("\n No student data available. \n")
        else:
            print("\n student list")
            for st in cls.student_list:
                st.dispaly()
            print()      
    @classmethod
    def delete_student(cls):
        roll=input("Enter Roll No to delete: ")
        for s in cls.student_list:
            if s.roll_no == roll:
                cls.student_list.remove(s)
                print("\n Student deleted ..")
                return
        print("\n student not founs! \n")

while True:
    print("======STUDENT MANAGEMENT SYSTEM=======")
    print("1. Add Student")
    print("2. Dispaly All Student")
    print("3. Delete Student")
    print("4. exit")

    choice=input("Enter your choice (1-4) : ")
    if choice == '1':
        Student.add_student()
    elif choice == '2':
        Student.dispaly_all()
    elif choice == '3':
        Student.delete_student()
    elif choice == '4':
        print("\n Exiting...!")
        break
    else:
        print("\n invalid choice! please enter 1-4.\n")