"""def is_palindrome(text: str) -> bool:
    #Check if a given string is a palindrome.
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    user_text = input("Enter a string: ")
    if is_palindrome(user_text):
        print(f"'{user_text}' is a Palindrome")
    else:
        print(f"'{user_text}' is Not a Palindrome")
"""

text = input("Enter string: ")

# space remove + lowercase
text = text.replace(" ", "").lower()

# reverse check
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")





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
