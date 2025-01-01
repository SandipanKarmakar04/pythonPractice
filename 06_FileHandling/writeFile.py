# # Write file
# f = open('myFile.txt', 'w')
# f.write("Hello")
# f.close()


# Open file in write mode ('w')
file = open('myFile.txt', 'w')
file.write("Hello, World!\n")  # Write a single line to the file
file.write("This is an example of the write() method.")
file.close()

# Read file
f = open('myFile.txt', 'r')
text = f.read()
print(text)
f.close()



