# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

from random import randint


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
ARRAY = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def counting_sort(array):
    
    min_item = min(array)
    max_item = max(array)
    
    count_lst = [0 for _ in range(max_item - min_item +1)]
    
    for i in array:
        count_lst[i-min_item] += 1
    
    index = 0
    for ind, el in enumerate(count_lst):
        for i in range(el):
            array[index] = ind + min_item
            index += 1

    return array


def lst_median(array):
    array = counting_sort(array)
    print(array)                   # Для наглядности
    
    if len(array) % 2 == 0:
        res = (array[len(array) // 2 -1] + array[len(array) // 2]) / 2
        return res
    else:
        return array[len(array) // 2]
        


print(ARRAY)
print(lst_median(ARRAY))
