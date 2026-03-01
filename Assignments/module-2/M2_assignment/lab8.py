# Write a Python program to create a function that takes a string as input and prints it. 
def mydata(id,name,city):

    print("id:",id)
    print("name:",name)
    print("city",city)

id=int(input("enter ID:"))
name=input("enter your name:")
city=input("enter your city:")
mydata(id,name,city)

#Write a Python program to create a calculator using functions. 
def addition(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return"can't divide by zero"
number1=int(input("enter first number: "))
number2=int(input("enter second number:"))

print("\n select operation:")
print("1.addition")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice=int(input("enter your choice: "))

if choice==1:
    print("result:",addition(number1,number2))
elif choice==2:
    print("result:",subtract(number1,number2))
elif choice==3:
    print("result:",multiply(number1,number2))
elif choice==4:
    print("result:",divide(number1,number2))
        
else:
        print("invalid choice")
