# bank_accounts.py

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return 0
        self.balance -= amount
        return amount

    def display_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

# Initialize a new bank account
account = BankAccount("John", "Doe", 123456, "Savings", 1234)

# Deposit $96
account.deposit(96)

# Withdraw $25
account.withdraw(25)

# Display the current balance
account.display_balance()