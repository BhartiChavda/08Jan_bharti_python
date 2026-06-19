"""Water Bill Calculation
User se water units lo:
• First 50 units → n3/unit
• Next 50 units → n5/unit
• Above 100 units → n8/unit
Total bill calculate karo"""


units = int(input("Enter water units: "))
bill = 0
if units > 100:
    bill = (units - 100) * 8
    units = 100
if units > 50:
    bill = bill + (units - 50) * 5
    units = 50
bill = bill + units * 3
print("Total Water Bill =", bill)

