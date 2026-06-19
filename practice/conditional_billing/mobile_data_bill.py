data = float(input("Enter data usage in GB: "))
bill = 0

if data <= 2:
    bill = 100
elif data <= 5:
    bill = 200
else:
    bill = 300

print(f"Bill amount: ₹{bill}")
