class studentinfo:
    def __init__(self,sid,name,city):
        self.sid = sid
        self.name = name
        self.city = city

studdata=[]

for i in range(2):
    sid=int(input("Enter student id: "))
    nm=input("Enter student name: ")
    ct=input("Enter student city: ")

    st=studentinfo(sid,nm,ct)
    studdata.append(st)

for i in studdata:
    print(i.sid)
    print(i.name)
    print(i.city)