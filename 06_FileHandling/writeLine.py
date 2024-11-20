try:
    with open("newFile2", 'x') as file:
        file.writelines(['line1\n','line2\n','line3\n','line4'])
    print("File has been created")
except:
    print("File already exist. Try another file name.")