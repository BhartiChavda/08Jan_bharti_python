n=int(input("enter number of students: "))
for i in range(n):
    print("\nstudent",i+1)
    nm=input("enter student name: ")
    sub=int(input("enter number of subject: " ))
    total=0

    for j in range(sub):
        marks=int(input(f"enter subject {j+1} marks: "))
        total+=marks
    per=total/sub

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


