from MemorySize import get_sizeof
import random

# Выбрал задачу 4 к третьему уроку.
# 4.Определить, какое число в массиве встречается чаще всего

# Windows 10 64bit
# Python 3.10 64 bit
ARRAY = [random.randint(0, 1000) for _ in range(1000)]

# Способ №2.
dct = {}
for i in ARRAY:
    if i not in dct.keys():
        dct[i] = 1
    elif i in dct.keys():
        dct[i] += 1
num, max_cnt = max(dct.items(), key=lambda x: x[1])
if max_cnt > 1:
    print(f'число {num} встречается чаще всего, {max_cnt} раз(а)')
else:
    print(f'все числа в массиве уникальны')


size_sum = get_sizeof(locals())
print(f'Объем занимаемой памяти состовляет {size_sum} байт')    # 43456

# Вывод. Создаётся дополнительный словарь. Используется 2n ОЗУ. 
