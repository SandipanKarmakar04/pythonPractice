'''QUESTION: Accepts name and birth_year during initialization. Automatically calculates the current age using another 
method calculate_age (assume the current year is 2024).'''

class Person:
    
    def __init__(self, name, birthYear):
        self.name = name
        self.birthYear = birthYear
   
    def calculate_age(self):
        currentYear = 2024
        age = currentYear - self.birthYear
        print(self.name,"your age is",age)

pers = Person("sandipan", 2000)
pers.calculate_age()

