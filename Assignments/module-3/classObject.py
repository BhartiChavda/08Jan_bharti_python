#class object
"""class student:   #create class 
    def __init__(self,a,b ):  #constructor define  
        self.a=a   
        self.b=b
    def display(self): #medthod define
        print("value a:",self.a)
        print("value b:",self.b)
        print(self.a + self.b)
try:
    a=int(input("enter value of a: "))
    b=int(input("enter value of b: "))
    data= student(a,b)
    data.display()
except Exception as e:
    print(e)"""

class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show_values(self):
        print("value of a:",self.a)
        print("value of b:",self.b)
class child(parent):
    def addition(self):
        print("addition is:",self.a + self.b)
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
data=child(a,b)
data.show_values()
data.addition()



