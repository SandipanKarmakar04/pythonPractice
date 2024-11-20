# Write file
f = open('myFile.txt', 'w')
f.write("Hello")
f.close()

# Read file
f = open('myFile.txt', 'r')
text = f.read()
print(text)
f.close()


