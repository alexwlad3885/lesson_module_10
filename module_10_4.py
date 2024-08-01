"""Домашнее задание по теме 'Очереди для обмена данными между потоками.'"""

import threading
from time import sleep
from queue import Queue

class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:

    num_list = []
    serve_list = []
    def __init__(self, tables):
        self.queue_one = Queue()
        self.queue_two = Queue()
        self.tables = tables
        self.customer_max = 20


    def customer_arrival(self):
        customer = 0
        for customer in range(self.customer_max):
            customer += 1
            print(f'Посетитель номер {customer} прибыл')
            sleep(1)
            Cafe.serve_customer(self, customer)

    def serve_customer(self, customer):
        serve_dict = {}
        num = customer
        Cafe.num_list.append(num)
        tables = self.tables

        if len(Cafe.num_list) <= self.customer_max:

            for i in tables:
                if i.is_busy == False:
                    print(f'Посетитель номер {num} сел за стол {i.number}')
                    i.is_busy = True
                    serve_dict[num] = i
                    Cafe.serve_list.append(serve_dict)
                    self.queue_one.put([num, i])
                    break

                elif i.is_busy == True and i.number < len(tables):
                    continue
                elif i.is_busy == True and i.number == len(tables):
                    print(f'Посетитель номер {num} ожидает свободный стол')
                    break


        # print(Cafe.num_list)
        # print(Cafe.serve_list)
        serve_dict = Cafe.serve_list[0]

        if len(Cafe.num_list) >= 6 and Cafe.num_list[0] in serve_dict:
            a, b = self.queue_one.get()
            Customer(a, b)
            Cafe.num_list = Cafe.num_list[1::]
            Cafe.serve_list[0] = Cafe.serve_list[1::]


class Customer:

    def __init__(self, customer, table):
        self.customer = customer
        self.table = table
        # sleep(5)
        print(f'Посетитель номер {self.customer} покушал и ушёл')
        self.table.is_busy = False


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)


# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
