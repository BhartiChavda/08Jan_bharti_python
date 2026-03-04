import datetime
fl=open("student.txt","a")
stno=int(input("enter number of student: "))
for i in range(stno):
    dt=datetime.datetime.now()
    stid=i+1
    stnm=input("enter student name: ")
    stcity=input("enter city: ")
    fl.write(f"date:{dt}\n id:{stid} \n name:{stnm} \n city:{stcity}\n")
    i+=i