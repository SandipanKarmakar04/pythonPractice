with open('myFile.txt', 'w') as f:
    f.write('I am inside withStatement')
with open('myFile.txt','r') as f:
    show = f.read()
    print(show)
