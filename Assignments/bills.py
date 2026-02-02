#1
"""units = int(input("Enter water units: "))
bill = 0
if units > 100:
    bill = (units - 100) * 8
    units = 100
if units > 50:
    bill = bill + (units - 50) * 5
    units = 50
bill = bill + units * 3
print("Total Water Bill =", bill)"""


#2
"""data = float(input("Enter data usage in GB: "))
if data <= 2:
    bill = 100
elif data <= 5:
    bill = 200
else:
    bill = 300
print("Mobile Data Bill =", bill)"""


#3
"""hours = int(input("Enter Parking Charges: "))
charges = 0
if hours > 5:
    charges = (hours - 5) *50
    hours = 5
if hours > 2:
    charges = charges + (hours -2) *40
    hours = 2
charges = charges + hours * 30
print("Total Parking Charges =", charges)"""

#4
"""usage = int(input("Enter monthly usage in GB: "))
if usage <= 100:
    bill = 500
elif usage <= 300:
    bill = 800
else:
    bill = 1200
print("Your Internet Bill is:", bill))"""

#5
"""distance= int(input("Enter distance in KM: "))
fare = 0
if distance > 15:
    fare = (distance - 15) * 20
    distance = 15
if distance > 5:
    fare = fare + (distance - 5) * 15
    distance = 5
fare = fare + distance *10
print("Total cab fare=", fare)"""


#6
"""units = int(input("Enter water units: "))
bill = 0
if units > 50:
    bill = (units - 50) * 10
    units = 50
if units > 20:
    bill = bill + (units - 20) * 8
    units = 20
bill = bill + units * 6
print("Total Water Bill =", bill)"""

#7
"""weight = float(input("Enter weight in KG: "))
charge=0
if weight >5:
    charge = 200
elif weight >1:
    charge = 100
else:
    charge = 50
print("Courier Charge is:", charge)"""

#8
"""num_subject = int(input("Enter number of subject: "))
fee=0
if num_subject >6:
    fee = 1200
elif num_subject >3:
    fee = 900
else:
    fee = 500
print("total exam fee is:", fee)"""

#9
"""v=input("enter vehicle type(bike,car,truck)")
dis= int(input("enter dis..."))
if v=="bike":
    rate=2
elif v=="car":
    rate=5
elif v=="truck":
    rate=10
else:
    print("enter valid type")
toll= dis*rate
print(toll)"""


#10
"""days = int(input("Enter number of days: "))
rent=0
if days >5:
    rent = (days-5)*1200
if days >2:
    rent = rent+(days-2)*1500
    days=2
rent=rent+days*2000
print("total hotel rent is:", rent)"""

"""for i in range(10,0,-1):
    print(i)"""

"""for i in range(1,6):
       for j in range(i):
         print(i, end="")
       print("")"""
"""
for i in range(1,6):
       for j in range(i):
         print(j+1, end="")
       print("")"""


"""for i in range(5,0,-1):
       for j in range(i):
         print("*",end="")
       print("")"""

"""for i in range(1,6):
       for j in range(i):
         print(chr(65+j),end=" ")
       print(" ")"""

n=1
for i in range(1,6):
       for i in range(i):
         print(n,end=" ")
         n+=1
       print(" ")

"""n=int(input("enter number: "))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")"""