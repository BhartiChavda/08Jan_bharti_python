students=[]
def add_student():
    id=int(input("Enter Student ID: "))
    name=input("enter student name: ")
    course=input("enter student course name: ")
    marks=int(input("enter student mark: "))

    student={
        "id": id,
        "name": name,
        "course": course,
        "marks": marks,
    }
    students.append(student)
    print("student add successfully!")

def view_student():
    if len(students)==0:
        print("no student found")
    else:
        for s in students:
            print("----------------------------------")
            print("ID :",s["id"])
            print("name :",s["name"])
            print("course :",s["course"])
            print("marks :",s["marks"])

def search_student():
    id=int(input("enter student ID: "))
    for s in students:
        if s["id"]==id:
            print(s)
            return
    print("student not found")

def update_student():
    id=int(input("enter student ID: "))
    for s in students:
        if s["id"]==id:
            s["name"]=input("enter new name: ")
            s["course"]=input("enter new course name: ")
            s["marks"]=int(input("enter new marks: "))
            print("student update successfully!")
            return
    print("student not found")
          
while True:
    print("\n__________________")
    print("1. add student")
    print("2. view atusent")
    print("3. search student")
    print("4. update student")
    print("0. exit")

    choice=input("enter choice: ")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif  choice=="3":
        search_student()
    elif  choice=="4":
        update_student()
    elif choice=="0":
        print("thankyou")
        break
    else:
        print("invalid choice")



