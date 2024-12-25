'''QUESTION: Create Account class with 2 attributes - balance and account no. Create methods for debit, credit 
and printing the balance'''

class Account:
    def __init__(self, balance, accountNo):
        self.balance = balance 
        self.accountNo = accountNo
    
    def debit(self,amount):
        self.balance -= amount
        print(amount,"was debited from your account",self.accountNo)
        print("your available abalance is: Rs.",self.balance)
    
    def credit(self,amount):
        self.balance += amount
        print(amount,"was credited to your account",self.accountNo)
        print("your available abalance is: Rs.",self.balance)

acc = Account(1000, 1234)
print(acc.balance)
acc.debit(100)
acc.credit(500)