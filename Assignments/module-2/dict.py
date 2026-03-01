#dict
"""subject={}
n=int(input("enter number of subject: "))
for i in range(n):
    subnm=input("enter subject name: ")
    marks=int(input("enter marks: "))
    subject[subnm]=marks
print(subject)"""

"""subject={}
n=int(input("enter number of subject: "))
for i in range(n):
    subnm=input("enter subject name: ")
    marks=int(input("enter marks: "))
    subject[subnm]=marks
print(subject)"""


"""data={}
n =int(input("enter number of subject: "))
for i in range(n):
    data[i]={
    "subject": input("enter subject name: "),
    "mark": int(input("enter marks: "))
    }
    
print(data)"""



"""stdata={}

n= int(input("enter number of student: "))
for i in range(n):
        id=int(input("enter id: ")),
        name=input("enter name: "),
        city=input("enter city: ")
        stdata[id]={
                "name":name,
                "city":city
        }
print(stdata)"""


stdata={}

n= int(input("enter number of student: "))
for i in range(n):
    id=int(input("enter id: "))
    stdata[id] ={
        
        "name":input("enter name: "),
        "city":input("enter city: ")
    }

print(stdata)


#f
"""stdata=[
    {'id', 'name','city'}
      ]
n=int(input("enter number of data"))
for i in range(n):
    id=int(input("enter id number: "))
    stdata.add(id)
    name=input("enter student name: ")
    stdata.append(name)
    city=input("enter city name: ")
    stdata.append(city)
print(stdata)"""


