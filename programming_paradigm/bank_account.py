# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self._account_balance = initial_balance  # Initialize _account_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount > self._account_balance:
            return False  # Insufficient funds
        else:
            self._account_balance -= amount
            return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
