text = input("Enter string: ")
result = ""
for ch in text:
    if ch != " ":
        result += ch
print(result)