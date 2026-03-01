#Write a Python program to import the math module and use functions like sqrt(), ceil(), floor(). 
import math
number=float(input("enter a number: "))
sqrt=math.sqrt(number)
ceil=math.ceil(number)
floor=math.floor(number)

print("square root:",sqrt)
print("ceil value:",ceil)
print("floor value:",floor)

#Write a Python program to generate random numbers using the random module. 
import random
number=random.randint(1111,9999)
print(number)