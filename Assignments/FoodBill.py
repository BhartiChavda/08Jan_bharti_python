print("1 pizza ₹100")
print("2 sendwich ₹200")
print("3 samosa ₹70")
print("4 sushi ₹100")
print("5 pasta ₹250")

choice=int(input("enter your choice: "))
qty=int(input("enter your quantity: "))
item=""
price=0
if choice==1:
    item="pizaa"
    price=100
elif choice==2:
    item="sendwich"
    price=200
elif choice==3:
    item="samosa"
    price=70
elif choice==4:
    item="sushi"
    price=100
elif choice==5:
    item="pasta"
    price=250
else:
    print("enter valid choice")
total=price*qty
gst=(total*18)/100
final=total+gst


print("  BILL   ")
print("item:", item)
print("price:",price)
print("quantity:", qty)
print("gst:",gst)
print("final total:",final)



