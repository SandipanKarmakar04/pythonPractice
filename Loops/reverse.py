data = []

while True:
    val = input("Enter the value: ")
    data.append(val)
    
    r = input("Want to enter another value?? (y / n): ")

    if(r.casefold() == "n"):
        break

print("your list" , list(reversed(data)))