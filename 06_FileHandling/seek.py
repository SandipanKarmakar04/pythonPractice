with open('file.txt', 'r') as fName:
    fName.seek(10)

    data = fName.read(5)
    print(data)
    print(fName.tell())