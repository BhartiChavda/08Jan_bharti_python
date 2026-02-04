#tuple    
"""data=()
n =int(input("enter number of city: "))
for i in range(n):
    n=input("enter city name: ")
    data= data+(n,)

print(data)"""

data=[]
numcity =int(input("enter number of city: "))
for i in range(numcity):
    city=input("enter city name: ")
    data.append(city)
print(tuple(data))