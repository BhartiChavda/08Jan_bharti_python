vehicle_type = input("Enter vehicle type (Bike/Car/Truck): ").strip().lower()
distance = float(input("Enter distance in km: "))
toll = 0

if vehicle_type == "bike":
    toll = distance * 2
elif vehicle_type == "car":
    toll = distance * 5
elif vehicle_type == "truck":
    toll = distance * 10
else:
    print("Invalid vehicle type entered.")
    exit()

print(f"Total toll: ₹{toll}")
