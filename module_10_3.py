"""Домашнее задание по теме 'Блокировки и обработка ошибок'"""


from threading import Thread, Lock

lock = Lock()


class BankAccount:

    def __init__(self):
        self.amount = 0
        self.account = 1000

    def deposit(self, amount):
        self.amount = amount
        with lock:
            self.account += self.amount
            print(f'Deposited {self.amount}, new balance is {self.account}')
        return self.account

    def withdraw(self, amount):
        self.amount = amount
        with lock:
            self.account -= self.amount
            print(f'Withdrew {self.amount}, new balance is {self.account}')
        return self.account


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100,))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
