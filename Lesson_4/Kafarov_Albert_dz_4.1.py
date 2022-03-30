# Задача 4 к третьему уроку.
# 4.Определить, какое число в массиве встречается чаще всего

import random
from timeit import timeit
import cProfile

SIZE_1 = 10
SIZE_2 = 100
SIZE_3 = 1000
SIZE_4 = 10000

MIN_ITEM = 0
MAX_ITEM = 1000
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_1)]
array_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
array_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]
array_4 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_4)]

# создал сразу 4 списка разной длины. Timeit буду тестировать на четырех списках, cProfile на четвертом, самом объемном

# Способ 1.
# Цикл в цикле, сложность O(n**2). Экономия по памяти
def max_cnt_num(array):
    num = ''
    max_cnt = 1
    for i in array:
        cnt = 0
        for n in array:
            if i == n:
                cnt += 1
        if max_cnt < cnt:
            num = i
            max_cnt = cnt
        cnt = 0

    if max_cnt > 1:
        return f'число {num} встречается чаще всего, {max_cnt} раз(а)'
    else:
        return f'все числа в массиве уникальны'


print('Вывод способа 1.\n')
print(max_cnt_num(array_4))
print(timeit('max_cnt_num(array_1)', globals=globals(), number=1000))     # 0.006704900064505637
print(timeit('max_cnt_num(array_2)', globals=globals(), number=1000))     # 0.452597500057891
print(timeit('max_cnt_num(array_3)', globals=globals(), number=1000))     # 42.54217309993692
# print(timeit('max_cnt_num(array_4)', globals=globals(), number=1000))     # Слишком долго


cProfile.run('max_cnt_num(array_4)')
'''         4 function calls in 6.708 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    6.708    6.708 <string>:1(<module>)
        1    6.708    6.708    6.708    6.708 Kafarov_Albert_dz_4.1.py:23(max_cnt_num)
        1    0.000    0.000    6.708    6.708 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''


# Способ 2.
# Создам дополнительный словарь. Ключами в нем будут значения из списка, а значениями количество повторений(счетчик значений)
# Сложность O(2n). Сложность по памяти O(2n) если не ошибаюсь
def max_cnt_num_2(array):
    dct = {}
    for i in array:
        if i not in dct.keys():
            dct[i] = 1
        elif i in dct.keys():
            dct[i] += 1
    num, max_cnt = max(dct.items(), key=lambda x: x[1])
    if max_cnt > 1:
        return f'число {num} встречается чаще всего, {max_cnt} раз(а)'
    else:
        return f'все числа в массиве уникальны'

print('Вывод способа 2.\n')
print(max_cnt_num_2(array_4))
print(timeit('max_cnt_num_2(array_1)', globals=globals(), number=1000))     # 0.007850199937820435
print(timeit('max_cnt_num_2(array_2)', globals=globals(), number=1000))     # 0.05067580007016659
print(timeit('max_cnt_num_2(array_3)', globals=globals(), number=1000))     # 0.3512299000285566
print(timeit('max_cnt_num_2(array_4)', globals=globals(), number=1000))     # 3.2537453999975696

cProfile.run('max_cnt_num_2(array_4)')
'''         20006 function calls in 0.011 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
        1    0.008    0.008    0.011    0.011 Kafarov_Albert_dz_4.1.py:61(max_cnt_num_2)
     1001    0.000    0.000    0.000    0.000 Kafarov_Albert_dz_4.1.py:68(<lambda>)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
    18999    0.002    0.000    0.002    0.000 {method 'keys' of 'dict' objects}'''


# Способ 3.
# Воспользуемся встроенной функцией max
# Сложность снова O(n**2)
def max_cnt_num_3(array):
    num = max(array, key=array.count)
    return num


print('Вывод способа 3.\n')
print(max_cnt_num_3(array_4))
print(timeit('max_cnt_num_3(array_1)', globals=globals(), number=1000))     # 0.0025331999640911818
print(timeit('max_cnt_num_3(array_2)', globals=globals(), number=1000))     # 0.17597849993035197
print(timeit('max_cnt_num_3(array_3)', globals=globals(), number=1000))     # 15.832497199997306
# print(timeit('max_cnt_num_3(array_4)', globals=globals(), number=1000))     # Слишком долго


cProfile.run('max_cnt_num_3(array_4)')
'''         5 function calls in 1.600 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.600    1.600 <string>:1(<module>)
        1    0.000    0.000    1.600    1.600 Kafarov_Albert_dz_4.1.py:99(max_cnt_num_3)
        1    0.000    0.000    1.600    1.600 {built-in method builtins.exec}
        1    1.600    1.600    1.600    1.600 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''


# Вывод.
# 2й Способ единственный справился с четырмя тестами timeit за адекватное время, но использует дополнительную память
# и вызывает многократно вызывает функцию lambda и метод keys словаря. 
# 1й и 3й методы имеют геометрическую прогрессию по времени выполнения в зависимости от объема входных данных. 
# Но функция max показывает лучшее время в timeit (видимо связано с кривизной моих рук, и тем что max наверное написан на плюсах)
# и значения в cProfile (хотя я не знаю на сколько одекватно cProfile показывает работу функций на плюсах)
