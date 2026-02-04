"""data=[]
n =int(input("enter number of subject: "))
for i in range(n):
    subject=input("enter subject name: ")
    data.append(subject)
print(data)"""
    
data=()
n =int(input("enter number of city: "))
for i in range(n):
    n=input("enter city name: ")
    data= data+(n,)

print(data)


