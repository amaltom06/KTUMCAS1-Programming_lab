# Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("\nDeposition Successful!")
        else:
            print("\nInvalid amount!")
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
            print("New Balance : ",self.balance)
        elif amount > self.balance:
            print("Not possible to withdraw. Insufficient funds.")
        else:
            print("Invalid amount!")
    def get_balance(self):
        return self.balance
account1 = BankAccount("3456", "amal", "Savings", 1000)
print("current balance:",account1.get_balance())
deposit_amount = float(input("Enter the deposit amount: "))
account1.deposit(deposit_amount)
withdrawal_amount = float(input("Enter the withdrawal amount: "))
account1.withdraw(withdrawal_amount)
account1.get_balance()