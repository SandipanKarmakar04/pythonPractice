class Student:

    country = "India" #it is class attribute.
    #funtion/method
    def add(self, a, b):
        return a + b

    #default constructor
    def __init__(self):
        print("I am default")

    #parameterized constructor
    def __init__(self, fn, ln):
        self.fname = fn #it is object attribute.
        self.lname = ln #it is object attribute.

s1 = Student("Sandipan", "Karmakar")
print(s1.fname, s1.lname)
print(s1.country)

s2 = Student("Priya", "Ghosh")
print(s2.fname, s2.lname)
print(s2.country)

print(s1.add(2,3))
