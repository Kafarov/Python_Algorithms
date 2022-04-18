from MemorySize import get_sizeof
import random

# Выбрал задачу 4 к третьему уроку.
# 4.Определить, какое число в массиве встречается чаще всего

# Windows 10 64bit
# Python 3.10 64 bit
ARRAY = [random.randint(0, 1000) for _ in range(1000)]


# Способ №3.
a_set = set(ARRAY)

most_common = None
cnt_most_common = 0

for item in a_set:
    cnt = 0
    for i in ARRAY:
        if item == i:
             cnt += 1
    if cnt > cnt_most_common:
        qty_most_common = cnt
        most_common = item


print(most_common)
print(get_sizeof(locals()))     # 58436


# Вывод. Было интересно посмотреть на разницу со словарём. 
# Самый не оптимальный вариант асимптотика O(n**2), в худшем случае. Затраты по памяти больше 2n.
