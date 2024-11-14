number = int(input("Enter the number for factorial: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("Factorial result is: ",factorial)
