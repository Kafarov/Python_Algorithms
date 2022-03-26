# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

ind_min = 0
num_min = 0
ind_max = 0
num_max = 0
for el, i in enumerate(array):
    if i > num_max:
        num_max = i
        ind_max = el
    if i <= num_min:
        num_min = i
        ind_min = el

array[ind_min], array[ind_max] =  num_max, num_min
print(array)

