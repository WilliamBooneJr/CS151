#Billy Boone
#This program creates an object "BankAccount" with instance variables "acct_number", "acct_holder, and "balance".
#Methods include get acct_holder name, depost, withdraw, get balance, transfer
#(transfers amount from b to recipient using withdraw and deposit methods and prints message)
#str method returns a string representation of the object

import stdio

class BankAccount:
    def __init__(self, acct_number, acct_holder, balance=0):
        self._acct_number = acct_number
        self._acct_holder = acct_holder
        self._balance = balance


# get account holder name method

    def get_acct_holder(self):
        return f"Account holder name: {self._acct_holder}"

# deposit method that updates balance and prints message
    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self._balance += amount
            return f"Deposit of {amount} successful. New balance: ${self._balance}"

#withdraw method that updates balance and prints message

    def withdraw(self, amount):
        if amount < 0 or amount > self._balance:
            return "Invalid withdrawal amount"
    
        else:
            self._balance -= amount
            return f"Withdrawal of {amount} successful. New balance: ${self._balance}"
    
# get balance method that returns balance

    def get_balance(self):
        return f"Current balance: {self._balance}"

    def __str__(self):
        return f"Account number: {self._acct_number}\nAccount holder: {self._acct_holder}\nBalance: ${self._balance}"

# transfer method that transfers amount from b to recipient using withdraw and deposit methods and prints message
#outputs error if recipient is not a BankAccount object

    def transfer(self, recipient, amount):
        if self._balance < amount:
            return "Insufficient funds"
        elif amount < 0:
            return "Invalid transfer amount"
        
        self.withdraw(amount)
        recipient.deposit(amount)
        return f"Transfer of ${amount} from {self._acct_holder} to {recipient._acct_holder} successful. New balance: ${self._balance}"

# test client 
    
def main():
    stdio.writeln("**Creating account for Bob and returning results")
    a = BankAccount(12345, "Bob Ross", 1000)
    stdio.writeln(a.__str__())

    stdio.writeln("**Creating account for Jane and returning results")
    b = BankAccount(54321, "Jane Doe", 500)
    stdio.writeln(b.__str__())

    stdio.writeln("**Testing invalid deposit ammount")
    stdio.writeln(a.deposit(-100))

    stdio.writeln("**Testing invalid withdrawal amount(negative and overdraft)")
    stdio.writeln(a.withdraw(-100))
    stdio.writeln(a.withdraw(100000))

    stdio.writeln("**Testing valid deposit and withdrawal amounts")
    stdio.writeln(a.deposit(1000))
    stdio.writeln(a.withdraw(300))
    stdio.writeln(a.__str__())

    stdio.writeln("**Testing get account holder name method")
    stdio.writeln(a.get_acct_holder())

    stdio.writeln("**Testing get balance method")
    stdio.writeln(a.get_balance())

    stdio.writeln("**Testing invalid transfer method")
    stdio.writeln(a.transfer(b, 10000))
    stdio.writeln(a.transfer(b, -100))
    
    stdio.writeln("**Testing valid transfer method")
    stdio.writeln(a.transfer(b, 100))






if __name__ == '__main__':
    main()
