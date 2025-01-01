try:
    with open("newFile2", 'w') as file:
        file.writelines(['line1\n','line5\n','line3\n','line4'])
    print("File has been created")
except:
    print("File already exist. Try another file name.")