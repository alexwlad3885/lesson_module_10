"""Домашнее задание по теме 'Блокировки и обработка ошибок'"""


from threading import Thread, Lock

lock = Lock()


class BankAccount:

    def __init__(self):
        self.amount = 0
        self.account = 1000

    def deposit(self, amount):
        self.account += amount
        return self.account

    def withdraw(self, amount):
        self.account -= amount
        return self.account


def deposit_task(*args):
    amount = args[1]
    account.account = args[0]
    for i in range(5):
        with lock:
            account.account = account.deposit(amount)
            print(f'Deposited {amount}, new balance is {account.account}')


def withdraw_task(*args):
    amount = args[1]
    if account.account == args[0]:
        account.account = args[0]
    for j in range(5):
        with lock:
            account.account = account.withdraw(amount)
            print(f'Withdrew {amount}, new balance is {account.account}')


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account.account, 100,))
withdraw_thread = Thread(target=withdraw_task, args=(account.account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
