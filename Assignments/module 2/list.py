#list
"""data=[]
n =int(input("enter number of subject: "))
for i in range(n):
    subject=input("enter subject name: ")
    data.append(subject)
print(data)"""



#list example
student=[]
studno=int(input("how many student to add: "))
for i in range(studno):
    studnm=input("enetr student name: ")
    student.append(studnm)
print(student)

search_stud=input("search student name: ")
if search_stud==studnm:
    print(search_stud,"student found")
else:
    print(search_stud,"student not found")


