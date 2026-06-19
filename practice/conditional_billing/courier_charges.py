weight = float(input("Enter weight in kg: "))
charge = 0

if weight <= 1:
    charge = 50
elif weight <= 5:
    charge = 100
else:
    charge = 200

print(f"Courier charge: ₹{charge}")
