class BankAccount:
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated= authenticated
    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
        else:
            self.authenticated = False

    def deposit(self, amount,username, password):
        if self.authenticated:
            if amount < 0:
                raise Exception("Deposit must be positive")
            self.balance += amount
        raise Exception("Not authenticated")

    def withdraw(self, amount):
        if self.authenticated:
            if amount < 0:
                raise Exception("Withdraw must be positive")
            self.balance -= amount
        raise Exception("Not authenticated")
# Part II : Minimum balance account

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance=0):
        BankAccount.__init__(self, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw, balance would be lower than minimum balance")
        BankAccount.withdraw(self, amount)

# Part III: Expand the bank account class