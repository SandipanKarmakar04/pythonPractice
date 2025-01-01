data = []

while True:
    val = input("Enter the value: ")
    data.append(val)
    
    r = input("Want to enter another value?? (y / n): ")

    if(r.casefold() == "n"):
        break

#data.reversed()  Reverse the list in place

print("your list" , list(reversed(data))) #it doesn't modify the actual data just print in reversed order