# x-api-key:“25540708-019e-4c84-8177-7d7959f5ea7a”
import json

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.account_type = ""
        self.balance = 0
        self.password = ""
        self.get_account()

    def get_account(self):
        with open('database.json', 'r') as db_file:
            data = json.load(db_file)
            accounts = data['accounts']
            for account in accounts:
                if account['account_holder'] == self.account_holder:
                    self.balance = account['balance']
                    self.account_type = account['account_type']
                    self.password = account['password']
                    break

    def save_changes(self):
        with open('database.json', 'r') as db_file:
            data = json.load(db_file) # load the database file into data
            accounts = data['accounts']
            for account in accounts:
                if account['account_holder'] == self.account_holder: # loop until account found
                    account['balance'] = self.balance # update balance of the current user
                    break
        # then overwrite entire file with updated data
        with open('database.json', 'w') as db_file:
            db_file.seek(0)
            json.dump(data, db_file, indent=2)

    def check_balance(self):
        print(f"Balance: ${self.balance}")
        print(f"Type: {self.account_type} Account")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.balance = round(self.balance, 2) # round to two decimal points
            print(f"Deposited ${amount}. New balance: ${self.balance}")
            self.save_changes()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        acc_type = self.account_type
        if amount > 0:
            if acc_type=="Savings" and amount > (self.balance - 100.00):
                print("Insufficient balance. Your remaining balance should be $100 minimum.")
            
            elif acc_type=="Checking" and amount > self.balance:
                print("Insufficient balance.")
            
            else:
                self.balance -= amount
                self.balance = round(self.balance, 2)
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
                self.save_changes()
        else:
            print("Withdrawal amount must be positive.")
