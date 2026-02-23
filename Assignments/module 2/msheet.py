"""msheet=[]

def studdata(id,name,nsub,mrk):
    total=sum(mrk)
    high=max(mrk)
    low=min(mrk)
    per=total/nsub



    print("id",id)
    print("name",name)
    print("subject",nsub)
    print("marks",mrk)

    

n=int(input("enter number of student:"))

for i in range(n):
    id=int(input("enter id: "))
    name=input("enter name:")
    nsub=int(input("enter number of subject:"))
    mrk=[]
    
    for j in range(nsub):
        mark=int(input(f"subject{j+1} mark: "))
        mrk.append(mark)
    studdata(id,name,nsub,mrk)
    total=sum(mrk)
    per=total/nsub
    high=max(mrk)
    low=min(mrk)
    msheet.append([id,name,nsub,mrk,total,per,high,low])


print(msheet)"""
import pandas

msheet=[]

def studdata(id,name,nsub,mrk):
    total=sum(mrk)
    high=max(mrk)
    low=min(mrk)
    per=total/nsub

    print("id",id)
    print("name",name)
    print("subject",nsub)
    print("marks",mrk)
    for i in range(len(mrk)):
        print(nsub, i+1, ":", mrk[i])

    print("Total:", total)
    print("Percentage:", per)
    print("Highest:", high)
    print("Lowest:", low)
    print("------------------")

    

n=int(input("enter number of student:"))

for i in range(n):
    id=int(input("enter id: "))
    name=input("enter name:")
    nsub=int(input("enter number of subject:"))
    mrk=[]
    
    for j in range(nsub):
        mark=int(input(f"subject{j+1} mark: "))
        mrk.append(mark)
    studdata(id,name,nsub,mrk)
    total=sum(mrk)
    per=total/nsub
    high=max(mrk)
    low=min(mrk)
    msheet.append({
        "id": id,
        "name": name,
        "subjects": nsub,
        "marks": mrk,
        "total": sum(mrk),
        "percentage": sum(mrk) / len(mrk),
        "highest": max(mrk),
        "lowest": min(mrk)
    })


df=pandas.DataFrame(msheet)
print("\t student marksheet")
print(df)

