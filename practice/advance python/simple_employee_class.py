class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name, self.salary)
e1 = Employee("Rahul", 50000)
e1.display()