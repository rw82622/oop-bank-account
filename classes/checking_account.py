from classes.account import Account

class checkingAccount(Account):
    def __init__(self, id, initial_bal, open_date, owner=None):
        super().__init__(id, initial_bal, open_date, owner)
        self.checks_used = 0
        
    def withdraw(self, amount):
        if self.balance > (amount + 1):
            super().withdraw(amount+1)
        else:
            return f"Warning: Insufficient funds. Current balance: {self.balance}"
        return f"Current balance: {self.balance}"
        
    def withdraw_using_check(self, amount):
        if self.checks_used < 3:
            if ((self.balance - amount) >= -10):
                self.balance -= amount
                self.checks_used += 1
            else:
                return("Warning: Insufficient funds.")
        else:
            if ((self.balance - (amount+2)) >= -10):
                self.balance -= (amount+2)
                self.checks_used += 1
            else:
                return("Warning: Insufficient funds.")
        return f"{self.balance}"
    
    def reset_checks(self):
        self.checks_used = 0