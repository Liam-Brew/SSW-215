
class Bank(object):

    def __init__(self, account_list):

        self.account_list = account_list

        self.txt_file = open("Result.txt", "w")
        self.txt_file.write("Initial State:\n" + self.account_list_to_str() + "\n")

    def withdrawal(self, slave_acc_number, master_acc_number, value):

        slave_account = self.find_account(slave_acc_number)
        master_account = self.find_account(master_acc_number)

        write_str = slave_account.name + " tried to withdraw $" + str(value) + "     \t"

        if slave_account.can_withdraw(value):
            write_str += "Withdrawal successful\n"
            slave_account.withdraw(value)
            master_account.withdraw(value * 2)
            for account in self.account_list:
                if account.account_number != master_acc_number and account.account_number != slave_acc_number:
                    account.deposit(value)
        else:
            write_str += "\tWithdrawal unsuccessful\n"
            slave_account.penalty_total += 5
            master_account.deposit(5)

        self.update_withdrawal_limits()

        self.txt_file.write(write_str + self.to_string() + "\n")

    def find_account(self, some_acc_number):
        for account in self.account_list:
            if account.account_number == some_acc_number:
                return account
        return None

    def account_list_to_str(self):
        str_ret = ""
        for account in self.account_list:
            str_ret += account.to_string() + "\n"
        return str_ret

    def close_txt(self):
        self.txt_file.close()

    def update_withdrawal_limits(self):
        for account in self.account_list:
            account.update_withdrawal_limit()

    def to_string(self):
        str_ret = ""
        for account in self.account_list:
            str_ret += "name: " + str(account.name) + "\n"
            str_ret += "\tbalance: " + str(account.balance) + "\n"
            str_ret += "\taccount_number: " + str(account.account_number) + "\n"
            str_ret += "\twithdrawal_limit: " + str(account.withdrawal_limit) + "\n"
            str_ret += "\twithdrawal_total: " + str(account.withdrawal_total) + "\n"
            str_ret += "\tdeposit_total: " + str(account.deposit_total) + "\n"
            str_ret += "\tpenalty_total: " + str(account.penalty_total) + "\n"
        return str_ret
