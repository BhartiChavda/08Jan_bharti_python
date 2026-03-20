#Write a Python program to create a class and access its properties using an object. 
class Student:

    def __init__(self, name, age, grade):
        self.name = name    
        self.age = age     
        self.grade = grade  

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Grade: {self.grade}")


student1 = Student("Bharti", 21, "A")
student2 = Student("Riya", 19, "B")

print("Details of Student 1:")
student1.display_info()

print("\nDetails of Student 2:")
student2.display_info()