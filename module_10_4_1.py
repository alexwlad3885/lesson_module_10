import threading
import queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer:
    def __init__(self, number):
        self.number = number

    def serve(self, table):
        table.is_busy = True
        print(f'Посетитель номер {self.number} сел за стол {table.number}')
        sleep(5)
        table.is_busy = False
        print(f'Посетитель номер {self.number} покушал и ушёл')


class Cafe:
    def __init__(self, tables):
        self.queue = None
        self.tables = tables

    def customer_arrival(self, customer_max=20):
        Cafe.queue = queue.Queue(customer_max)
        for i in range(1, customer_max + 1):
            customer = Customer(i)
            print(f'Посетитель номер {customer.number} прибыл')
            if not Cafe.queue.empty():
                Cafe.queue.put(customer)
                print(f'Посетитель номер {customer.number} ожидает свободный стол')
                sleep(1)
                customer = Cafe.queue.get()
                if Cafe.serve_customer(self, customer):
                    Cafe.queue.task_done()
            elif not Cafe.serve_customer(self, customer):
                Cafe.queue.put(customer)
                print(f'Посетитель номер {customer.number} ожидает свободный стол')
            sleep(1)

        while not Cafe.queue.empty():
            customer = Cafe.queue.get()
            if Cafe.serve_customer(self, customer):
                Cafe.queue.task_done()

    def serve_customer(self, customer):
        for table in tables:
            if not table.is_busy:
                threading.Thread(target=customer.serve, args=(table,)).start()
                return True
            else:
                continue
        return False


if __name__ == '__main__':

    # Создаем столики в кафе
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]
    #
    # # Инициализируем кафе
    cafe = Cafe(tables)    #
    #
    # Запускаем поток для прибытия посетителей
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    # Ожидаем завершения работы прибытия посетителей
    customer_arrival_thread.join()
