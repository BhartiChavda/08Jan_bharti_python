arr = [12, 5, 7, 1, 20]
small = arr[0]
for i in arr:
    if i < small:
        small = i
print("Smallest:", small)