# Practical Examples: Method Overloading and Overriding
#Example 1: Method Overloading
print("\n>>> Method Overloading Example <<<")
class Calculator:
    def add(self, a, b=0, c=0):
        result = a + b + c
        print("Sum:", result)
calc = Calculator()
calc.add(5, 3)   
calc.add(5, 3, 2)   
calc.add(10)       

# Example 2: Method Overriding
print("\n>>> Method Overriding Example <<<")
class Parent:
    def show(self):
        print("This is the parent class method")
class Child(Parent):
    def show(self):
        print("This is the child class method (Overridden)")
child_obj = Child()
child_obj.show()     