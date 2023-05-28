class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{self.owner}'s account is created with a balance of {self.balance}")

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'

    def deposit(self, dep_amount):
        self.balance += dep_amount
        return f'Deposit Accepted. Your new balance is {self.balance}'

    def withdraw(self, with_amount):
        if with_amount <= self.balance:
            self.balance -= with_amount
            return f'Withdrawal Accepted. Your new balance is {self.balance}'
        else:
            return f'Sorry, insufficient funds. You current balance is {self.balance}'


# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
acct1.owner
# 4. Show the account balance attribute
acct1.balance
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)