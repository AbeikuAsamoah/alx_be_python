class BankAccount():
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        """Deduct amount if sufficient funds exist, else return False"""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format"""
        print(f"Current Balance: ${self.account_balance:.2f}")
