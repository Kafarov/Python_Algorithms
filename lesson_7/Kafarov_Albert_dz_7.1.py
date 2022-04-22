# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, з
# аданный случайными числами на промежутке [-100; 100). 
# Выведите на экран исходный и отсортированный массивы 

from random import randint


MIN_ITEM = -100
MAX_ITEM = 100


def bubble_sort (array):
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    
    cnt = len(array) -1
    
    for _ in range(len(array)):
        for i in range(cnt):
            
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        cnt -= 1
    return array


array = [randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(20)]

print(array)
print(bubble_sort(array))
