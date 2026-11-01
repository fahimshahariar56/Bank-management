import json 
import random
import string 
from pathlib import Path


class Bank:
    Database = 'Data.json'
    data = []


    # Load data from the JSON file if it exists
    try:
        if Path(Database).exists():
            with open(Database, 'r') as fs:
                data = json.load(fs)
        else: 
            print("No such file exist")
    except Exception as err:
        print(f"An error occurred as {err}")  


    # update the JSON file with the current data
    @classmethod
    def __update_json(cls):
        with open(cls.Database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    # create a new account
    def create_account(self):
        print("Creating a new account...")

        print("Please provide the following information:")

        info = {
            'name' : input("Enter your name: "),
            'age' : int(input("Enter your age: ")),
            'gender' : input("Enter your gender: "),
            'account_number' : ''.join(random.choices(string.digits, k=10)),
            'pin' : int(input("Enter a 4-digit PIN: ")),
            'balance' : 0.0,
            'transaction' : []
        }

        if info['age'] >= 18 and len(str(info['pin'])) == 4 and str(info['pin']).isdigit():
            Bank.data.append(info)
            Bank.__update_json()
            print("Account created successfully!")
        else:
            print("Invalid input. Please enter a valid age (18 or above) and a 4-digit PIN.")

    # view account details
    def view_account(self):
        account_number = input("Enter your account number: ")
        Pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i['account_number'] == account_number and i['pin'] == Pin ]

        print('your account details are as follows:')

        for i in userData[0]:
            print(f"{i}: {userData[0][i]}")


    # deposit money into the account
    def deposit_money(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [
            i for i in Bank.data
            if i['account_number'] == account_number
            and i['pin'] == pin
        ]

        if not userData:
            print("Invalid account number or PIN!")
            return

        print("Enter the amount you want to deposit:")
        amount = float(input())

        if amount <= 0:
            print("Invalid amount!")
            return

        account = userData[0]

        # Update balance
        account['balance'] += amount

        # Create transactions list if it doesn't exist
        if 'transactions' not in account:
            account['transactions'] = []

        # Add transaction history
        account['transactions'].append({
            'type': 'Deposit',
            'amount': amount,
            'balance': account['balance']
        })

        # Update JSON file
        Bank.__update_json()

        print(f"Deposited {amount} successfully.")
        print(f"New balance: {account['balance']}")

    

    # withdraw money from the account
    def withdraw_money(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        
        userData = [i for i in Bank.data if i['account_number'] == account_number and i['pin'] == pin]
        
        print('Enter the amount you want to withdraw:')
        amount = float(input())
        
        for i in userData[0]:
            if i == 'balance':
                userData[0][i] -= amount
                print(f"Withdrew {amount} successfully. New balance: {userData[0][i]}")
                Bank.__update_json()

    # update account information
    def update_account(self):
        
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i['account_number'] == account_number and i['pin'] == pin]

        print("Updating account information...")
        
        newdata = {
            "name": input("Enter your new name: "),
            "pin": int(input("Enter your new 4-digit PIN: ")),
            "gender": input("Enter your new gender: ")
        }

        if len(str(newdata['pin'])) == 4 and str(newdata['pin']).isdigit():
            userData[0]['name'] = newdata['name']
            userData[0]['pin'] = newdata['pin']
            userData[0]['gender'] = newdata['gender']


            Bank.__update_json()
            print("Account information updated successfully!")


    # delete an account
    def delete_account(self):

        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i['account_number'] == account_number and i['pin'] == pin]

        if userData:
            check = input("Are you sure you want to delete your account? (y/n): ").lower()
            if check == 'y':
                    Bank.data.remove(userData[0])
                    Bank.__update_json()
                    print("Account deleted successfully.")
            elif check == 'n':
                print("Account deletion canceled.")
            else:
                print("Invalid input. Account deletion canceled.")    
        else:
            print("Account not found or incorrect PIN.")


    # check account balance
    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        userData = [i for i in Bank.data if i['account_number'] == account_number and i['pin'] == pin]

        if userData:
            print(f"Your current balance is: {userData[0]['balance']}")
            Bank.__update_json()

        else:
            print("Account not found or incorrect PIN.")



    # transfer money to another account
    def transfer_money(self):
        sender_account_number = input("Enter your account number: ")
        sender_pin = int(input("Enter your PIN: "))

        sender_data = [i for i in Bank.data if i['account_number'] == sender_account_number and i['pin'] == sender_pin]

        if not sender_data:
            print("Sender account not found or incorrect PIN.")
            return

        receiver_account_number = input("Enter the recipient's account number: ")
        receiver_data = [i for i in Bank.data if i['account_number'] == receiver_account_number]

        if not receiver_data:
            print("Recipient account not found.")
            return

        amount = float(input("Enter the amount to transfer: "))

        if sender_data[0]['balance'] < amount:
            print("Insufficient balance for the transfer.")
            return

        # Perform the transfer
        sender_data[0]['balance'] -= amount
        receiver_data[0]['balance'] += amount

        Bank.__update_json()
        print(f"Transferred {amount} successfully. New balance: {sender_data[0]['balance']}")



    # change_pin
    def change_pin(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))

        user_data = [i for i in Bank.data if i['account_number'] == account_number and i['pin'] == pin]

        new_pin = int(input("Enter your new 4-digit PIN: "))
        retype_new_pin = int(input("Retype your new PIN: "))
        
        if user_data:
            if len(str(new_pin)) == 4 and len(str(retype_new_pin)) == 4 and new_pin == retype_new_pin:
                user_data[0]['pin'] = new_pin
                Bank.__update_json()
                print("PIN updated successfully!!")

            else: 
                print("PIN dosen't matched !! try aging...")

    # transaction_history
    def transaction_history(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        
        user_data = [i for i in Bank.data if i['account_number'] == account_number and i['pin'] == pin]
        
        account = user_data[0]
        
        if 'transaction' not in account or not account['transaction']:
            print("No transaction history found.")
            return 

        print("\n========== TRANSACTION HISTORY ==========")
        
        for transaction in account['transaction']:
            print(f"Type   : {transaction['type']}")
            print(f"Amount : {transaction['amount']}")
            print(f"Balance: {transaction['balance']}")
            print("-" * 40)
            
            
            
            
# Bank Management System
user = Bank()

print("Welcome to the Bank Management System")
print("Please select an option:")
print("1. Create a new account")
print("2. View account details")
print("3. Deposit money")
print("4. Withdraw money")
print("5. Update account information")
print("6. Delete account")
print("7. Check account balance")
print("8. Transfer money")
print("9. Transaction history")
print("10. Change PIN")
print("11. Search account")
print("12. Account statement")
print("13. Exit")


check = int(input("Enter your choice (1-13): "))

if check == 1:
    user.create_account()

if check == 2:
    user.view_account()    

if check == 3:
    user.deposit_money()    

if check == 4:
    user.withdraw_money()    

if check == 5:
    user.update_account()    

if check == 6:
    user.delete_account()

if check == 7:
    user.check_balance()

if check == 8:
    user.transfer_money()

if check == 9:
    user.transaction_history()

if check == 10:
    user.change_pin()

if check == 11:
    user.search_account()

if check == 12:
    user.account_statement()

if check == 13:
    print("Thank you for using the Bank Management System.")
    exit()