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

#Insert Data
"""insert_data="insert into studentinfo(name,city)values('bharti','rajkot')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

#update record
update_data="UPDATE studentinfo SET name='krupa' WHERE id=1"

try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)

#Delete Data
"""delete_data="delete from studentinfo where id=1"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""
    
#Show Data
show_data="select * from studentinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)
    
    for i in data:
        print(i)
except Exception as e:
    print(e)
