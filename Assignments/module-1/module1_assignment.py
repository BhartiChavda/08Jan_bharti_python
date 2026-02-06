#lab 1
"""print("Hello, World!")

name=input("enter your name: ")
print("my nazmed is", name)"""

#lab 2
# It uses proper indentation, comments, and variables
"""f_number = int(input("Enter first number: "))
s_number = int(input("Enter second number: "))

# Calculate the sum of two numbers
total = f_number + s_number

# Display the result
print("Sum =", total)"""



#lab 3
#Write a Python program to demonstrate the creation of variables and different data types. 
"""b=23 #integer int
print(b)
b1=23.2#float 
print(b1)
b2=True#boolean bool
print(b2)
name="bharti chavda"#string
print(name)

# Practical Example 1: How does the Python code structure work? 
# Input section
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# calculate (process)
sum = a + b
# Output section
print("Sum =", sum)

#Practical Example 2: How to create variables in Python? 
# Program to create variables in Python
name = "Bharti"
age = 20
percentage = 85.5
is_active = True
print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)
print("Active:", is_active)


#Practical Example 3: How to take user input using the input() function. 
name=input("enter your name: ")
age=int(input("enter your age: "))
print(name)

#Practical Example 4: How to check the type of a variable dynamically using type(). 
a = 10
b = 5.5
c = "Python"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))"""


#lab 4
"""#Practical Example 5: Write a Python program to find greater and less than a number using if_else. 
num = int(input("Enter a number: "))
if num>10:
    print("Number is greater than 10")
else:
    print("Number is less than or equal to 10")

#Practical Example 6: Write a Python program to check if a number is prime using if_else.  
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")
#Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.
mark=int(input("enter your mark: "))
if mark>=90:
    print("Grade A")
elif mark>=80:
    print("Grade B")
elif mark>=70:
    print("Grade c")
elif mark>=60:
    print("Grade d")
else:
    print("fail")
#Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if. 
age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
if age >= 18:
    if weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible (Weight less than 50)")
else:
    print("Not eligible (Age less than 18)")"""

#lab 5

#Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango'] 
"""List1 = ['apple', 'banana', 'mango'] 
for i in List1:
    print(i)"""


# Practical Example 2: Write a Python program to find the length of each string in List1. 
"""List1 = ['apple', 'banana', 'mango'] 
for i in List1:
    print(i,":", len(i))"""

#Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition. 
"""List1 = ['apple', 'banana', 'mango'] 
search_list=input("enter item name: ")
for i in List1:
    if i== search_list:
        print(search_list)
        break
else:
        print("item not found")"""

#Practical Example 4: Print this pattern using nested for loop: 
"""markdown 
Copy code 
* 
** 
*** 
**** 
***** """

"""for i in range(1,6):
     for j in range(i):
      print("*", end="")
     print()"""


#lab 8
#Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango'] 
"""List1 = ['apple', 'banana', 'mango'] 
for i in List1:
    if i== "banana":
       continue
    print(i)"""

#Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement. 
"""List1 = ['apple', 'banana', 'mango'] 
for i in List1:
    if i == "banana":
       break
    print(i)"""


#lab 9
# Write a Python program to demonstrate string slicing. 
"""name="bharti ravjibhai chavda"
print(name[10])
print(name[7:16])
print(name[-10])
print(name[10:])
print(name[:16])
"""
# Write a Python program that manipulates and prints strings using various string methods. 
"""name="bharti chavda"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.istitle())
print(name.split())  
"""
