import random
balance=7000
class bank:
    def account(self):
         self.acnum=random.randint(1111,9999)
         self.acnm=input("enter holder name: ")
         self.actype=input("enter account type: ")
         
class deposite(bank):
     def deposite(self):
          global balance
          am_depo=int(input("enter ammount deposite:"))
          if am_depo>=2000:
               balance +=am_depo
               print(f"ammount deposited successfully balance:{balance}")
          else:
               print("minimum deposite is 2000")


class withdrwal(deposite):
     def withdrwal(self):
          global balance
          amount=int(input("enter withdrwal ammount: "))
          if amount>balance:
               print("insufficient balance")
          else:
               balance-= amount
               print(f"withdrawal successful remaining balance:{balance}")


class statement(withdrwal):
     def statement(self):
          print("------------ACCOUNT DETAILS-------------")
          print("account number:",self.acnum)
          print("account holder name:",self.acnm)
          print("account type:",self.actype)
          print("total balance:",balance)
          
          
data=statement()
data.account()  
data.deposite()
data.withdrwal()
data.statement()

             
          
          
        