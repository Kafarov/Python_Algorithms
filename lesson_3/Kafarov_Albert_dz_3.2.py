# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Способ с рекурсией
def even_item_id(lst, id_lst=[], cnt=0):
    if lst[0] % 2 == 0:
        id_lst.append(cnt)
    cnt += 1
    lst = lst[1:]
    return even_item_id(lst, id_lst, cnt) if len(lst) else id_lst


print(even_item_id(array))

# Способ с циклом
even_id = []
for i, el in enumerate(array):
    if el % 2 == 0:
        even_id.append(i)

print(even_id)

# Способ с циклом №2. То же самое записанное в 1 строку
print([i for i, el in enumerate(array) if el % 2 == 0])
