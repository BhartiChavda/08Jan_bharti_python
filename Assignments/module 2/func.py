"""def mydata():
    print("my name is bharti chavda")
mydata()

def sum(a,b):
  print(a+b)
sum(23,34)"""


"""def mydata(id,name,city):

    print("id:",id)
    print("name:",name)
    print("city",city)

id=int(input("enter ID:"))
name=input("enter your name:")
city=input("enter your city:")
mydata(id,name,city)"""



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




