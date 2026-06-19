subjects = int(input("Enter number of subjects: "))
fee = 0

if subjects <= 3:
    fee = 500
elif subjects <= 6:
    fee = 900
else:
    fee = 1200

print(f"Total exam fee: ₹{fee}")
