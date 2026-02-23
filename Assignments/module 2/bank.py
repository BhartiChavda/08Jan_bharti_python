"""balance=7000
def bank():
    acnum=int(input("enter account number: "))
    acnm=input("enter holder name: ")
    actype=input("enter account type: ")
    return acnum,acnm,actype
    
def deposite():
    global balance
    am_depo=int(input("enter ammount deposite:"))
    if am_depo>=2000:
        print("ammount deposite")
        return am_depo
    else:
        print("min 2000")
        return 0

def withdrwal():
    global balance
    amount=int(input("enter withdrwal ammount: "))
    if amount>balance:
        print("insufficient balance")
    
    else:
        balance=balance-amount
        print("withdrwal successful")
        
    
def statement(acnum,acnm,actype,balance):
    print("--------account details-------")
    print("account number:",acnum)
    print("account holder name:",acnm)
    print("account type:",actype)
    print("total balance: ",balance)
    
        
acnum,acnm,actype=bank()
deposite()
withdrwal()
statement(acnum,acnm,actype,balance)"""


balance=7000

def bank1():
    acnum=int(input("enter account number: "))
    acnm=input("enter holder name: ")
    actype=input("enter account type: ")
    return acnum,acnm,actype
    
    
def deposite():
    global balance
    am_depo=int(input("enter ammount deposite:"))
    if am_depo>=2000:
        print("ammount deposite")
        
    else:
        print("min 2000")
        

def withdrwal():
    global balance
    amount=int(input("enter withdrwal ammount: "))
    if amount>balance:
        print("insufficient balance")
    
    else:
        balance=balance-amount
        print("withdrwal successful")
        
        
    
def statement(acnum,acnm,actype):
    global balance
    print("--------account details-------")
    print("account number:",acnum)
    print("account holder name:",acnm)
    print("account type:",actype)
    print("total balance: ",balance)
    
        




