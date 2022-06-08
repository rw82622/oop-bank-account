from classes.owner import Owner
from classes.account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.all_accounts = Account.all_accounts()
        self.all_owners = Owner.all_owners()
        
    def list_accounts(self):
        for index, item in enumerate(self.all_accounts):
            print(f"{index+1}. {item.__dict__}")
            
    def list_owners(self):
        for index, item in enumerate(self.all_owners):
            print(f"{index+1}. {item.__dict__}")
            