from bank import * 
balance=5000
acnum,acnm,actype=bank1()
while True:
    print("1. deposite")
    print("2. withdrwal")
    print("3. statement")
    print("4. exit")
    choice=int(input("enter your choice: "))

    if choice==1:
        deposite()
    elif choice==2:
        withdrwal()
    elif choice==3:
        statement(acnum,acnm,actype)
    elif choice==4:
        print("thank you")
        break
        

    else:
        print("invalid choice")