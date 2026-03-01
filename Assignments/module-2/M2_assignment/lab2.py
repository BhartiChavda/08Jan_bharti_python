#Write a Python program to add elements to a list using insert() and append(). 
data=[]
n=int(input("enter number of student: "))
for i in range(n):
    id=int(input("enter student id: "))
    name=input("enter student name: ") 
    per=float(input("enter your per: "))
    data.append([id,name,per])
print(data)

#Write a Python program to remove elements from a list using pop() and remove(). 
data=[1,"bharti",20.4,True]
print(data)
data.pop(0)
data.remove("bharti")
print(data)