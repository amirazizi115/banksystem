# x-api-key:“25540708-019e-4c84-8177-7d7959f5ea7a”
from bank_account import BankAccount
import json

def login():
    print("--------------------")
    print("Welcome to the Bank Account System!")
    
    while True:
        account_holder = input("Enter account holder name: ")
        password = input("Enter your password: ")

        # Try to find the account and verify the password
        with open('database.json', 'r') as db_file:
            data = json.load(db_file)
            accounts = data['accounts']
            for account_data in accounts:
                # Just find matching account_holder & password
                if account_data['account_holder'] == account_holder and account_data['password'] == password:
                    print("Login successful!")
                    return account_holder

        print("Invalid username/password. Try again.")  # Prompt again if login fails

def main():
    account_holder = login()
    account = BankAccount(account_holder) # Create the bank account instance

    # Allow the user to perform actions after login
    while True:
        print("--------------------")
        print("\n1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Choose an option >> ")

        if choice == "1":
            print("--------------------")
            account.check_balance()
        
        elif choice == "2":
            print("--------------------")
            amount = float(input("Enter amount to deposit: $"))
            amount = round(amount,2) # round to two decimal points
            account.deposit(amount)
        
        elif choice == "3":
            print("--------------------")
            amount = float(input("Enter amount to withdraw: $"))
            amount = round(amount,2)
            account.withdraw(amount)
        
        elif choice == "4":
            print("--------------------")
            print("Logging out...")
            print("You have been logged out.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
