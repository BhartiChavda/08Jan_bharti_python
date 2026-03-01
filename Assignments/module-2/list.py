#list
"""data=[]
n =int(input("enter number of subject: "))
for i in range(n):
    subject=input("enter subject name: ")
    data.append(subject)
print(data)"""



#list example
"""student=[]
studno=int(input("how many student to add: "))
for i in range(studno):
    studnm=input("enetr student name: ")
    student.append(studnm)
print(student)

search_stud=input("search student name: ")
if search_stud==studnm:
    print(search_stud,"student found")
else:
    print(search_stud,"student not found")"""




# take 5 inputs and append
# print using loop
# calculate total
# # find max and min
"""🎯 Task:
Create an empty list called marks
Ask user to enter 5 subject marks
Store them in the list
Print all marks using a for loop
Find and print:
Total marks
Highest mark
Lowest mark"""
#try
"""marks=[]
nmarks=int(input("enter total marks: "))
for i in range(nmarks):
    nmark=int(input("enter marks: "))
    marks.append(nmark)
print(marks)
print(sum(marks))
print(max(marks))
print(min(marks))"""




"""student={}

numstud=int(input("enter number of student: "))
for i in range(numstud):
    nmsub=input("enter name of student: ")
    nstud=int(input("enter number of subject: "))
    marks=[]
    for j in range(1,nstud+1):
        mrk=int(input("subject" +str(j)+ "\tmark: "))
        marks.append(mrk)
        student[nmsub]=marks
print(student)"""


data=[]
n=int(input("enter number of subject: "))
for i in range(n):
    nmsub=input("enter subject name: ")
    data.append(nmsub)
print(data)

 



