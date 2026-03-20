#Write a Python program to read the contents of a file and print them on the console. 
file = open("example.txt", "r")
content = file.read()
print("Contents of the file:")
print(content)

file.close()

# Write a Python program to write multiple strings into a file. 

file = open("multilines.txt", "w")

file.write("This is the first line.\n")
file.write("This is the second line.\n")
file.write("This is the third line.\n")
file.close()

print("Multiple strings have been written to the file successfully.")