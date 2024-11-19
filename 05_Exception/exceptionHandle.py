try:
    x = int(input("enter a value"))
    y = int(input("enter a value"))
    add = x + y
    print(add)
except ValueError as e:
    print("Invalid entry.")
else:
    print("Your desired output is here.")
finally:
    print("Thank you for your effort.")



# Understanding Exceotions.
#   a) ZeroDivisionError: Dividing by zero.
#   b) ValueError: Invalid conversion of data type.
#   c) FileNotFoundError: File operations fails because the file doesn't exist.

# Cleaning up with 'finally'.
#   The finally block is executed no matter what, whether an exception occurs or not.
#   It is often used for cleaning operations like closing files or releasing resources.