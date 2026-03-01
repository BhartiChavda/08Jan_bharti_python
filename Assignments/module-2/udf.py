data=[]
def studdata(id,name,sub):
    print("id",id)
    print("name",name)
    print("subject",sub)

n=int(input("enter number of student:"))

for i in range(n):
    id=int(input("enter id: "))
    name=input("enter name:")
    sub=input("enter subject:")
    studdata(id,name,sub)
    data.append({
        "id":id,
        "name":name,
        "subject": sub})
print(data)

 

"""data=[]

def studdata(id,name,sub):
    print("id",id)
    print("name",name)
    print("subject",sub)

n=int(input("enter number of student:"))

for i in range(n):
    id=int(input("enter id: "))
    name=input("enter name:")
    sub=input("enter subject:")
    studdata(id,name,sub)
    data.append([id,name,sub])


print(data)"""

