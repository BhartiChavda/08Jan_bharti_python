#Write a Python program to update a value in a dictionary. 
student={"id": 101,"name":"bharti","city":"rajkot","age":21,"course":"BCA","grade":"B"}
student["id"]=204
print("Update Dictionary:\n",student)

#Write a Python program to merge two lists into one dictionary using a loop.
list1=["id","name","age","city"]
list2=[204,"bharti",21,"rajkot"]
list={}
for i in range(len(list1)):
    list[list1[i]]=list2[i]
print("Merged Dictionary:")
print(list)