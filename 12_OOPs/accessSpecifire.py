class Bank:
    def __init__(self,accountNo, password):
        self.accountNo = accountNo
        self.__password = password
    
    def resetPass(self):
        print(self.__password)

b = Bank(12345, "abcde")
print(b.accountNo)
print(b.resetPass())
