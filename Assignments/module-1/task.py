firstname=input("enter first name: ")
lastname=input("enter last name: ")
email=input("enter email ID: ")
mobile=input("enter mobile number: ")
password=input("enter password: ")
confirmpassword=input("enter confirm password: ")

if firstname.isalpha():
    print(firstname)
else:
    print("enter only alphabets")
    
if lastname.isalpha():
    print(lastname)
else:
    print("enter only alphabets")

if email.islower():
    print(email)
else:
    print("enter only lowercase")
if mobile.isdigit():
    print(mobile)
else:
    print("enter only digit")

if len(password)>=8 and  len(password)<=12:
     print(password)
else:
    print("length shoud be min 8 and max 12 char")

if password==confirmpassword:
    print(confirmpassword)
else:
    print("password do not match")




