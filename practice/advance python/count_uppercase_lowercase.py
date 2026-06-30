text = input()
upper = 0
lower = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

check=input("enter string: ")
upper=0
lower=0
for i in check:
    if i.isupper():
        upper +=1
    elif i.lower():
        lower +=1
print("upper case:",upper)
print("lower case: ",lower)