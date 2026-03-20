#Write a Python program to search for a word in a string using re.search(). 
import re
print("\n>>> Example 1: re.search() <<<")
text1 = "My name is Bharyi Chavda"
pattern1 = "name"
result1 = re.search(pattern1, text1)
if result1:
    print(f"Word '{pattern1}' found in the string!")
else:
    print(f"Word '{pattern1}' not found in the string!")


# Example 2: Match a word at the beginning using re.match()
print("\n>>> Example 2: re.match() <<<")
text2 = "Python programming is fun"
pattern2 = "Python"
result2 = re.match(pattern2, text2)
if result2:
    print(f"Word '{pattern2}' matched at the beginning of the string!")
else:
    print(f"Word '{pattern2}' did not match at the beginning.")