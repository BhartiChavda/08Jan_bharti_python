"""for i in range(10,0,-1):
    print(i)"""

"""for i in range(1,6):
       for j in range(i):
         print(i, end="")
       print("")"""
"""
for i in range(1,6):
       for j in range(i):
         print(j+1, end="")
       print("")"""


"""for i in range(5,0,-1):
       for j in range(i):
         print("*",end="")
       print("")"""

"""for i in range(1,6):
       for j in range(i):
         print(chr(65+j),end=" ")
       print(" ")"""

n=1
for i in range(1,6):
       for i in range(i):
         print(n,end=" ")
         n+=1
       print(" ")