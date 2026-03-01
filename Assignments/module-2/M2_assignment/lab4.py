#Write a Python program to create a tuple with multiple data types. 
data=(1,"bharti",20.4,True)
print(data)
print("integer:",data[0])
print("string:",data[1])
print("float:",data[2])
print("boolean:",data[3])


data=(1,"bharti",20.4,True)
print("Tuple:", data)
for i in data:
    print(i, type(i))

#Write a Python program to concatenate two tuples. 
data1=(1,"bharti",20.4,True)
data2=(2,"shivansh",28.11,False)
concat=data1+data2
print("Concatenated tuple:",concat)