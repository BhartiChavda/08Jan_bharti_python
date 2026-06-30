#odd even
num=int(input("enter number: "))
if num%2==0:
    print("even")
else:
    print("odd")

#positive negative zero
num=int(input("enter number: "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#Eligible for Voting
age=int(input("enter age: "))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")

#Largest of Two Numbers
num1=int(input("enter first num: "))
num2=int(input("enter second num: "))
if num1>num2:
    print("largest",num1)
else:
    print("largest", num2)

#Smallest of Two Numbers
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
if num1<num2:
    print("smallest",num1)
else:
    print("smallest",num2)


##Largest of Three Numbers
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
n3=int(input("enter 3rd number: "))

if n1>=n2 and n1>=n3:
    print("largest",n1)
elif n2>=n1 and n2>=n3:
    print("largest",n2)
else:
    print("largest",n3)

#Divisible by 5
num=int(input("enter number: "))
if num%5==0:
    print("divisible by 5 ")
else: 
    print("not divisible by 5")

#Divisible by 5 and 11
num=int(input("enter number: "))
if num%5==0 and num %11==0:
    print("divisible by 5 and 11 ")
else: 
    print("not divisible by 5 and 11")

#Leap Year
year=int(input("enter year: "))
if (year %400==0) or(year%4==0 and year%100 !=0):
    print("leap year")
else:
    print("not leap year")

#Pass or Fail
marks=int(input("enter marks: "))
if marks>=35:
    print("pass")
else:
    print("fail")

#Grade System 
marks=int(input("enter marks: "))
if marks>=90:
    print("A grade")
elif marks>=75:
    print("B grade")
elif marks>=60:
    print("C grade")
elif marks>=35:
    print("pass")
else:
    print("fail")


#Character is Vowel or Consonant
ch=input("enter charecter: ")
if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

#Alphabet or Not
alpha=input("enter alphabet: ")
if ('a'<= alpha <='z') or('A'<=alpha <='Z'):
    print("alphabet")
else:
    print("not alphabet")

#Number is 3 Digit or Not
num=int(input("enter number: "))
if 100<=num<=999:
    print("3 digit number")
else:
    print("not 3 digit number")

#Check Even and Positive
num=int(input("enter number: "))
if num>0 and num%2==0:
    print("positive even number")
else:
    print("not positive even number")

#Both numbers are equal
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
if num1==num2:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

#smallest 3 number
n1=int(input("enter 1st number: "))
n2=int(input("enter 2nd number: "))
n3=int(input("enter 3rd number: "))

if n1<n2 and n1<n3:
    print(f"{n1} number is smallest")
elif n2<n1 and n2<n3:
    print(f"{n2} number is smallest")
else:
    print(f"{n3} number is smallest")

#leap year
year=int(input("enter year: "))
if (year%400==0) or (year%4==0 and year%100 !=0):
    print("366 days")
else:
    print("365 days")

#check charecter lower and upper 
ch=input("enter charecter: ")
if 'a'<=ch<='z':
    print("lowercase charecter")
elif 'A'<=ch<='Z':
    print("uppercase charecter")
else:
    print("enter valid charecter")

#divisible 2 and 3 
num=int(input("enter number: "))
if num%2==0 and num%3==0:
    print("number divisible by both")
else:
    print("number not divisible by both")

#salary
salary=int(input("enter salary: "))
if salary>50000:
    print("high salary")
elif salary>30000:
    print("medium salary")
else:
    print("low salary")

#age category
age=int(input("enter age: "))
if age>=60:
    print("Senior Citizen")
elif age>=20 and age<=59:
    print("adult")
elif age>=13 and age<=19:
    print("teenager")
else:
    print("child")


#units 
units=int(input("enter units: "))
if units<100:
    print("low consumption")
elif units>100 and units<300:
    print("medium consumption")
else: 
    print("high consumption")


#S_marksheet 
m1=int(input("enter theory mark: "))
m2=int(input("enter practical mark: "))

