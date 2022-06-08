from account import Account

class SavingsAccount(Account):
    def __init__(self,id, initial_bal, open_date, owner=None):
        if initial_bal > 10:
            super().__init__(id, initial_bal, open_date, owner=None)
        else:
            print('A new savings account cannot be created with an initial balance less than $10.')
    
    def withdraw(self, amount):
        if self.balance > (amount + 12):
            super().withdraw(amount+2)
        else:
            print("Warning: Insufficient funds.")
            return f"${self.balance}"
        
    def add_interest(self, rate):
        interest_amount = (rate/100) * self.balance 
        interest_amount = round(interest_amount, 2)
        self.balance += interest_amount
        return f"${interest_amount}"
