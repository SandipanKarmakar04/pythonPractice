try:
    with open("newFile", 'x') as nfile:
        nfile.write("This is a newly created file")
    print("Your file has been created")
except:
    print("File already exist.")