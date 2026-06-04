text = input("Enter a string: ") #Takes a string input from the user.
rev = ""  #Initializes an empty string to store the reversed version of the input string.
for ch in text:  #Loops through each character in text. ch represents the current character.
    rev = ch + rev  #Appends the current character to the beginning of the reversed string.
print(rev)  #Prints the reversed string.