"""Домашнее задание по теме "Создание потоков"."""

from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()


def wite_words(word_count, file_name):
    count_max = word_count
    file = open(file_name, mode='w', encoding='utf8')
    count = 0
    while count < count_max:
        for i in range(count_max):
            count += 1
            str_file = f'Какое-то слово № {count}'
            file.write(str_file + '\n')
            sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

time_start = datetime.now()

thr_1 = Thread(target=wite_words, args=(10, 'example5.txt',))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt',))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt',))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt',))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
