class Person:
    name = "anonymous"
    
    # def changeName(self,name):
    #     # self.name = name
    #     # Person.name = name
    #     self.__class__.name = "Karmakar"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("sandipan")
print(p1.name)
print(Person.name)