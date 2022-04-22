# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

from random import uniform

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
ARRAY = [uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def merge_sort(lst):
    
    if len(lst) <= 1:
        return lst
    
    right = merge_sort(lst[len(lst)//2:])
    left = merge_sort(lst[:len(lst)//2])
    
    # Создадим доп саисок, но зато сможем пройтись одним циклом for
    # Хотел выиграть по времени, но timeit показал незначительный прирост производительности 
    sort_lst = []
    l = r = 0
    x = len(right) + len(left)
    
    for _ in range(x):
        try:
            if right[r] < left[l]:
                sort_lst.append(right[r])
                r += 1
            else:
                sort_lst.append(left[l])
                l += 1
        except IndexError:
            if len(right) > r:
                # Насколько я помню это не конкатенация
                sort_lst += right[r:]
                break
            else:
                sort_lst += left[l:]
                break
    
    return sort_lst

print(ARRAY)
print(merge_sort(ARRAY))
