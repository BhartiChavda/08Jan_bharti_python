# બધા students નો data store કરવા માટે empty list
students = []


# Student Add Function
def add_student():


    # User પાસેથી માહિતી લેવી
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    # Dictionary બનાવવી
    student = {
        "id": id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    # Dictionary ને list માં add કરવી
    students.append(student)

    print("Student Added Successfully")


# બધા Students જોવા માટે Function
def view_students():

    # જો list ખાલી હોય
    if len(students) == 0:
        print("No Student Found")

    else:
        # બધા students ને એક પછી એક print કરવા
        for s in students:
            print("----------------------")
            print("ID :", s["id"])
            print("Name :", s["name"])
            print("Age :", s["age"])
            print("Course :", s["course"])
            print("Marks :", s["marks"])


# Student Search Function
def search_student():

    # User પાસેથી ID લેવી
    id = int(input("Enter Student ID: "))

    # List માં search કરવું
    for s in students:

        # ID match થાય તો data બતાવવો
        if s["id"] == id:
            print(s)
            return

    # ID ન મળે તો
    print("Student Not Found")


# Student Update Function
def update_student():

    id = int(input("Enter Student ID: "))

    for s in students:

        if s["id"] == id:

            # નવી માહિતી લેવી
            s["name"] = input("Enter New Name: ")
            s["course"] = input("Enter New Course: ")
            s["marks"] = int(input("Enter New Marks: "))

            print("Student Updated Successfully")
            return

    print("Student Not Found")


# Student Delete Function
def delete_student():

    id = int(input("Enter Student ID: "))

    for s in students:

        if s["id"] == id:

            # List માંથી student delete કરવો
            students.remove(s)

            print("Student Deleted Successfully")
            return

    print("Student Not Found")


# Program ચાલુ રાખવા માટે Infinite Loop
while True:

    # Menu બતાવવું
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    # User પાસેથી Choice લેવી
    choice = input("Enter Choice: ")

    # Choice પ્રમાણે Function Call કરવું
    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")