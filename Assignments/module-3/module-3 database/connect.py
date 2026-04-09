import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="")
print(mydb)
print("connection establisted...")