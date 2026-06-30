text=input("enter string: ")
text=text.replace(" ","").lower()
if text ==text[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    



# number
num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10        # last digit
    reverse = reverse * 10 + digit
    num = num // 10         # remove last digit

if original == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")
