import pymysql


try:
    db=pymysql.connect(host="localhost",user="root",password="",database="testdb")
    print("database connected!")
except Exception as e:
    print(e)
cr=db.cursor()

#table create
tbl_create="create table studentinfo(id integer primary key auto_increment,name text,city text)"
try:
    cr.execute(tbl_create)
    print("table created!")
except Exception as e:
    print(e)

#insert function
def insert_data():
    n=int(input("enter number of insert record"))
    for i in range(n):
        name=input("enter student name: ")
        city=input("enter city: ")
        insert_data=f"insert into studentinfo(name,city)values('{name}','{city}')"
        cr.execute(insert_data)
    try:
        db.commit()
        print("Record inserted!")
    except Exception as e:
        print(e)

#update function
def update_data():
    id = int(input("Enter student id to update: "))
    name = input("Enter new name: ")
    city = input("Enter new city: ")

    update_query = f"update studentinfo set name='{name}', city='{city}' where id={id}"
    cr.execute(update_query)

    try:
        db.commit()
        print("Record updated!")
    except Exception as e:
        print(e)
        
#delete function
def deletedata():
    id = int(input("Enter student id to delete: "))
    delete_query = f"delete from studentinfo where id={id}"

    try:
        cr.execute(delete_query)
        db.commit()
        print("Record deleted!")
    except Exception as e:
        print(e)


while True:
    print("1. insert")
    print("2. update")
    print("3. delete")
    print("4. exit")

    choice=int(input("enter your choice: "))
    if choice==1:
        insert_data()
    elif choice==2:
        update_data()
    elif choice==3:
        deletedata()
    elif choice==4:
        print("thank you")
        break
    
    else:
        print("invalid choice")
