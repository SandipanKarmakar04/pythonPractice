# file = open('myFile2.txt', 'r')

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# file.close()

with open('myFile2.txt', 'r') as file:
    while True:
        l = file.readline()
        if not l:
            break
        print(l.strip()) # strip(): it removes the new line character
      