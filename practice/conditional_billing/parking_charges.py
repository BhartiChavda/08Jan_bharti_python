hours = int(input("Enter Parking Charges: "))
charges = 0
if hours > 5:
    charges = (hours - 5) *50
    hours = 5
if hours > 2:
    charges = charges + (hours -2) *40
    hours = 2
charges = charges + hours * 30
print("Total Parking Charges =", charges)