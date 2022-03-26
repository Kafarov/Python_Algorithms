# В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве. 
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». 
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = MIN_ITEM
ind_num = ''

for el, i in enumerate(array):
    if i < 0 and i >= num:
        num = i
        ind_num = el

print('знвчение', num, 'Позиция в массиве', ind_num)
        