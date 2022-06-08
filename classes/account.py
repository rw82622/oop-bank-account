class Account:
    list_of_all_accounts = []
    list_of_all_account_id = []
    def __init__(self,id, initial_bal, open_date, owner=None):
        initial_bal = int(initial_bal)
        if initial_bal < 0:
            raise Exception('A new account cannot be created with initial negative balance.')
        self.id = id
        self.balance = initial_bal
        self.open_date = open_date
        self.owner = owner
        Account.list_of_all_accounts.append(self)
        Account.list_of_all_account_id.append(self.id)
        
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print(f"Warning: Insufficient funds.")
        return f"Current balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return f"{self.balance}"
    
    def get_balance(self):
        return f"{self.balance}"
    
    def add_owner(self, owner):
        self.owner = owner
        
    @classmethod
    def all_accounts(Account):
        return Account.list_of_all_accounts
    
    @classmethod
    def find(Account, account_id):
        for item in Account.list_of_all_accounts:
            if int(item.id) == account_id:
                return item
            