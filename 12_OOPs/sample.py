# class Student:
#     def __init__(self):
#         print("hi i am init")

# s = Student()


# import priya
# credit = 1000
# debit = 500

# a = priya.sub(credit,debit)
# print(a)

try:
    a=10
    if a/0 == a:
        print("zero applicable")
except ZeroDivisionError as e:
    print(e)