"""Домашнее задание по теме 'Потоки на классах'"""


from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count = self.power
        number_of_days = 0
        count_max = 100
        while count_max > 0:
            count_max -= count
            number_of_days += 1
            print(f'{self.name} сражается {number_of_days} день(дня)..., осталось {count_max} воинов.')
            sleep(1)
        else:
            print(f'{self.name} одержал победу спустя {number_of_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
