
class Account(object):

    def __init__(self, name, balance, account_number):

        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.withdrawal_limit = .1 * balance

        self.starting_balance = balance
        self.withdrawal_total = 0
        self.deposit_total = 0
        self.penalty_total = 0

    def can_withdraw(self, value):
        if self.balance - value >= 0 and value <= self.withdrawal_limit:
            return True
        return False

    def withdraw(self, value):
        self.balance -= value
        self.withdrawal_total += value

    def deposit(self, value):
        self.balance += value
        self.deposit_total += value

    def update_withdrawal_limit(self):
        self.withdrawal_limit = .1 * self.balance

    def to_string(self):

        str_ret = str(self.name) + "\t\t"
        str_ret += str(self.balance) + "\t\t"
        str_ret += str(self.account_number)

        return str_ret
