class Student:

    def __init__(self,fn, marks):
        self.name = fn
        self.marks = marks

    def get_avg(self):

        sum = 0
        for i in self.marks:
            sum += i
        print("hello",self.name,"your average marks is:",sum/3)

s1 = Student("sandipan",[88, 85, 91])
s1.get_avg()

# s1.name = "sandipan karmakar" you can manipulate a value like this and can print accordingly.
# s1.get_avg() 

s2 = Student("priya",[88, 85, 91])
s2.get_avg()