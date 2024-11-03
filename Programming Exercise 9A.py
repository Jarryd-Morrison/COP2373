class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.02):
        """
        Initialize the bank account with owner's name, account number, initial amount, and interest rate.
        """
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        """
        Adjusts the interest rate for the account.
        """
        self.interest_rate = new_rate

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.amount += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account.
        """
        if 0 < amount <= self.amount:
            self.amount -= amount
        else:
            raise ValueError("Invalid withdrawal amount.")

    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.amount

    def calculate_interest(self, days):
        """
        Calculates interest for the specified number of days, based on the current balance and interest rate.
        Formula: Interest = Principal * Rate * (Days / 365)
        """
        daily_rate = self.interest_rate / 365
        interest = self.amount * daily_rate * days
        return interest

    def __str__(self):
        """
        Returns a string representation of the account balance and interest information.
        """
        return (f"Account holder: {self.name}\n"
                f"Account number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest rate: {self.interest_rate * 100:.2f}%")

# Test function for the BankAcct class
def test_bank_acct():
    # Create an account
    account = BankAcct(name="John Stewart", account_number="123456789", amount=1000.0, interest_rate=0.03)
    print("Initial account details:")
    print(account)
    
    # Test deposit
    print("\nTesting deposit of $800...")
    account.deposit(800)
    print("Updated balance after deposit:", account.get_balance())
    
    # Test withdrawal
    print("\nTesting withdrawal of $400...")
    account.withdraw(400)
    print("Updated balance after withdrawal:", account.get_balance())
    
    # Test interest calculation
    days = 30
    interest = account.calculate_interest(days)
    print(f"\nInterest for {days} days: ${interest:.2f}")
    
    # Test interest rate adjustment
    new_rate = 0.05
    print(f"\nAdjusting interest rate to {new_rate * 100}%...")
    account.adjust_interest_rate(new_rate)
    print("Updated account details with new interest rate:")
    print(account)


test_bank_acct()
