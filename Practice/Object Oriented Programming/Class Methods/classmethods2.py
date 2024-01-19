class BankAccount:
    interest_rate = 5.0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        return f"Balance for {self.account_holder}'s account: ${self.balance}"

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate


# Creating instances of BankAccount
account1 = BankAccount("Chitresh", 5000)
account2 = BankAccount("Vivek", 8000)

# Displaying initial balances and interest rate
print(account1.display_balance())
print(account2.display_balance())
print(f"Current Interest Rate: {BankAccount.interest_rate}%")

# Changing the interest rate using the class method
BankAccount.change_interest_rate(6.0)

# Displaying balances after changing the interest rate
print(account1.display_balance())
print(account2.display_balance())
print(f"Updated Interest Rate: {BankAccount.interest_rate}%")
