from classes.bank import Bank
from classes.account import Account
from classes.owner import Owner
from classes.checking_account import checkingAccount
from classes.savings_account import SavingsAccount
import csv

chase = Bank('JP Morgan Chase')

try:
    with open('./data/accounts.csv') as account_file:
        accounts_data = csv.reader(account_file)
        for current_line in accounts_data:
            new_account = Account(*current_line)
        print("Successfully created instances of the Account class using data from accounts.csv")
            
    with open('./data/owners.csv') as owner_file:
        owners_data = csv.reader(owner_file)
        for current_line in owners_data:
            new_owner = Owner(*current_line)
        print("Successfully created instances of the Owner class using data from owner.csv")
            
    with open('./data/account_owners.csv') as account_owners_file:
        account_owners_data = csv.reader(account_owners_file)
        for current_line in account_owners_data:
            matching_account_index = Account.list_of_all_account_id.index(current_line[0])
            matching_account = chase.all_accounts[matching_account_index]
            matching_account.owner = current_line[1]
        print("Successfully created instances of the Owner class using data from owner.csv")
        
    # chase.list_accounts()
    # myAccount = Account.find(15155)
    # myAccount.add_owner(25)
    # print(myAccount.owner)
    # my_checking_account = checkingAccount(82622, 1000, '2003-11-07 11:34:56 -0800', '14')
    # print(my_checking_account.get_balance())
    # print(my_checking_account.withdraw(100))
    # print(my_checking_account.get_balance())
except:
    print("Error in process.")