# create account class with 2 attributes-blance and account no.
# Create a method for debit,credit and print the balance


class Account():
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    def debit(self,amount):
        self.balance-=amount
        print("Debited amount is",amount)
        print("total balance is",self.get_balance())
    
    def credit(self,amount):
        self.balance+=amount
        print("Credited amount is",amount)
        print("total balance is",self.get_balance())
        
    def get_balance(self):
        return self.balance
            
        
acc1=Account(10000,123456)
acc1.debit(1000)
acc1.credit(500)
       