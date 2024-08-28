#create account class with 2 atrributes-balance & account no.create methids for debit,credit & printing the balance.
class Account:
    def __init__(self,bal,accno):
        self.balance=bal
        self.accountno=accno 
    
    def debit(self,amount):
        self.balance -= amount
        print(amount,"was debited")
        print("total balance",self.total_balance())
  
    def credit(self,amount):
        self.balance += amount
        print(amount,"was credited")
        print("total balance",self.total_balance())

    def total_balance(self):
        return self.balance

acc1=Account(50000,89705069)
print(acc1.balance)
print(acc1.accountno)
acc1.debit(5000)
acc1.credit(1)
acc1.total_balance()