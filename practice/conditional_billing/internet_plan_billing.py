usage = float(input("Enter monthly usage in GB: "))
bill = 0

if usage <= 100:
    bill = 500
elif usage <= 300:
    bill = 800
else:
    bill = 1200

print(f"Bill amount: ₹{bill}")
