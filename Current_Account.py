from account import Account

class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

CurrentAccount = CurrentAccount()
CurrentAccount.deposit(5000)
CurrentAccount.withdraw(1500)

