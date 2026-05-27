import sqlite3
try:
    db=sqlite3.connect("self.db")
    print("database connected!")
except Exception as e:
    print(e)

#table create
tbl_create="create table self1(id integer primary key autoincrement, name text, age integer, city text)"
try:
    db.execute(tbl_create)
    print("table craeted")
except Exception as e:
    print(e)

#insert data
"""insert_data="insert into self1(name, age, city)values('bharti',21,'rajkot'),('karina',17,'rajkot'),('vandana',16,'sardhar')"
try:
    db.execute(insert_data)
    db.commit()
    print("record inserted successfully!")
except Exception as e:
    print(e)"""

#update record
update_data="update self1 set city='rajkot' where id=3"
try:
    db.execute(update_data)
    db.commit()
    print("record updated successfully!")
except Exception as e:
    print(e)

#delete record
dlt_data="delete from self1 where id=3"
try:
    db.execute(dlt_data)
    db.commit()
    print("record deleted successfully!")
except Exception as e:
    print(e)

    #display data
dispaly_data="select * from self1"
try:
    cursor=db.execute(dispaly_data)
    rows=cursor.fetchall()
    print("dispay table")
    for row in rows:
        print(row)

except Exception as e:
    print(e)