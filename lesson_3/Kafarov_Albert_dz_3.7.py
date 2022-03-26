# В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

steck = []
for i in array:
    if len(steck) < 2:
        steck.append(i)
    elif i < steck[0]:
        steck[0] = i
    elif i < steck[1]:
        steck[1] = i

print(steck)
