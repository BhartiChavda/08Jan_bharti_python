units = float(input("Enter gas units: "))
bill = 0

if units <= 20:
    bill = units * 6
elif units <= 50:
    bill = (20 * 6) + ((units - 20) * 8)
else:
    bill = (20 * 6) + (30 * 8) + ((units - 50) * 10)

print(f"Total bill: ₹{bill}")
