import sqlite3
try:
    db=sqlite3.connect("mydemodb.db")
    print("database connected!")
except Exception as e:
    print(e)

#table create
tbl_create="create TABLE product(id INTEGER PRIMARY KEY AUTOINCREMENT, pname TEXT,price INTEGER,qty INTEGER)"
try:
    db.execute(tbl_create)
    print("table created!")
except Exception as e:
    print(e)

#insert record
insert_data="INSERT INTO product(pname,price,qty)VALUES ('mobile', 20000,2),('laptop', 67000,1),('TV', 45000,3),('PC', 10000,2),('iphone', 120000,1)"
try:
    db.execute(insert_data)
    db.commit()
    print("record inserted!")
except Exception as e:
    print(e)

update_data="UPDATE product SET price=98000 WHERE id=5"
try:
    db.execute(update_data)
    db.commit()
    print("record updated!")
except Exception as e:
    print(e)

dlt_data="DELETE FROM product WHERE id=4"
try:
    db.execute(dlt_data)
    db.commit()
    print("record deleted!")
except Exception as e:
    print(e)

    show_data="select * FROM product"
try:
    db.execute(show_data)
    db.commit()
    print("table show!")
except Exception as e:
    print(e)