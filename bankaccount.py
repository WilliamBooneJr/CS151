#Billy Boone
#This program creates an object "BankAccount" with instance variables "acct_number", "acct_holder, and "balance".
#Methods include get acct_holder name, depost, withdraw, get balance, transfer
#(transfers amount from b to recipient using withdraw and deposit methods and prints message)
#str method returns a string representation of the object

import stdio

class BankAccount:
    def __init__(self, acct_number, acct_holder, balance=0):
        self.acct_number = acct_number
        self.acct_holder = acct_holder
        self.balance = balance


# get account holder name method

def get_acct_holder(self):
    return f"Account holder name: ", self.acct_holder

# deposit method that updates balance and prints message
def deposit(self, amount):
    if amount < 0:
        return "Invalid deposit amount"
    else:
        self.balance += amount
        return f"Deposit of {amount} successful. New balance: {self.balance}"

#withdraw method that updates balance and prints message

def withdraw(self, amount):
    if amount < 0 or amount > self.balance:
        return "Invalid withdrawal amount"
    
    else:
        self.balance -= amount
        return f"Withdrawal of {amount} successful. New balance: {self.balance}"
    
# get balance method that returns balance

def get_balance(self):
    return f"Current balance: {self.balance}"

def __str__(self):
    return f"Account number: {self.acct_number}\nAccount holder: {self.acct_holder}\nBalance: {self.balance}"

# transfer method that transfers amount from b to recipient using withdraw and deposit methods and prints message
#outputs error if recipient is not a BankAccount object

def transfer(self, recipient, amount):
    self.withdraw(amount)
    recipient.deposit(amount)
    return f"Transfer of {amount} from {self} to {recipient} successful. New balance: {self.balance}"

# test client 
    




