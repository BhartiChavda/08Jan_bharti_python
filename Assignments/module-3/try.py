"""try:
    studid=int(input("enter student id: "))
    studnm=input("enter student name: ")
    print(studid,studnm)
except Exception as b:
    print(b)"""


"""try:
    studid=int(input("enter student id: "))
    studnm=input("enter student name: ")
    print(studid,studnm)
except:
    print("error")"""


try:
    studno=int(input("enter number of student: "))
    for i in range(studno):
        studid=int(input("enter student id:"))
        studnm=input("enter student name: ")
    print("student id:",studid)
    print("student name:",studnm)
except Exception as b:
    print(b)

finally:
    print(studno)

