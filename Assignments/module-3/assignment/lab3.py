# Write a Python program to open a file in write mode, write some text, and then close it. 

file = open("example.txt", "w")

file.write("Hello! This is a sample text written to the file.\n")
file.write("Python makes file handling easy.")
file.close()

print("Text has been written to the file successfully.")
