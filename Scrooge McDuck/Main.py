from Account import Account
from Bank import Bank


def main():

    huey_account_number = 700007
    dewey_account_number = 800008
    louie_account_number = 900009
    scrooge_account_number = 100001

    bank = Bank([Account("Huey Duck", 150, huey_account_number),
                 Account("Dewey Duck", 350, dewey_account_number),
                 Account("Louie Duck", 25, louie_account_number),
                 Account("Scrooge McDuck", 1000000, scrooge_account_number)])

    bank.withdrawal(louie_account_number, scrooge_account_number, 2)
    bank.withdrawal(dewey_account_number, scrooge_account_number, 20)
    bank.withdrawal(huey_account_number, scrooge_account_number, 20)
    bank.withdrawal(louie_account_number, scrooge_account_number, 10)
    bank.withdrawal(dewey_account_number, scrooge_account_number, 20)
    bank.withdrawal(huey_account_number, scrooge_account_number, 30)
    bank.withdrawal(louie_account_number, scrooge_account_number, 40)

    bank.close_txt()


main()
