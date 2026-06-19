days = int(input("Enter number of days: "))
rent = 0

if days <= 2:
    rent = days * 2000
elif days <= 5:
    rent = (2 * 2000) + ((days - 2) * 1500)
else:
    rent = (2 * 2000) + (3 * 1500) + ((days - 5) * 1200)

print(f"Total rent: ₹{rent}")
