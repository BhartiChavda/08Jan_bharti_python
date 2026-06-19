distance = float(input("Enter distance in km: "))
fare = 0

if distance <= 5:
    fare = distance * 10
elif distance <= 15:
    fare = (5 * 10) + ((distance - 5) * 15)
else:
    fare = (5 * 10) + (10 * 15) + ((distance - 15) * 20)

print(f"Total fare: ₹{fare}")
