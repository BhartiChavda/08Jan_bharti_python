m1=int(input("enter mark1: "))
m2=int(input("enter mark2: "))
m3=int(input("enter mark3: "))

if m1>=40 and m2>=40 and m3>=40:
    total=m1+m2+m3
    per=total/3

    print("total", total)
    print("per", per)
   
    if per>=80:
        print("Grade A")
    elif per>=60:
        print("Grade b")
    elif per>=40:
        print("Grade c")

else:
    print("you are fail")

