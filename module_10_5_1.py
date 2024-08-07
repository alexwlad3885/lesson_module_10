"""Домашнее задание по теме 'Многопроцессное программирование'"""
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf8') as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

time_start = datetime.now()

# Линейный вызов
for f_name in filenames:
    read_info(f_name)

# Многопроцессный
if __name__ == '__main__':
    with Pool() as pool:
        pool.map(read_info, filenames)

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

# 0:00:04.433979 (линейный вызов)
# 0:00:01.955491 (многопроцессорный вызов)
