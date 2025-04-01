# parent class with deposit function 
class BankAccount:
    def __init__(self,accountNumber,holderName,balance=1000):
        self.accountNumber=accountNumber
        self.holderName=holderName
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        return f"New balance added {amount} Total balance is {self.balance}"
    
# child class inherit Parent class all method 

class BankChild(BankAccount):
    def __init__(self,accountNumber,holderName):
        super().__init__(accountNumber,holderName)
    def withdraw(self,amount):
        if (amount>self.balance):
            print('Balance is excedded')
        self.balance-=amount
        return f'Withdraw balance {amount} remaining balance {self.balance}'
    

b1=BankChild(12334,'Jobayed')
print(b1.deposite(3400))
print(b1.deposite(3400))
print(b1.withdraw(2000))