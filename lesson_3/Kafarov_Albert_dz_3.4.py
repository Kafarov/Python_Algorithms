# 4.Определить, какое число в массиве встречается чаще всего

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

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
    print('число', num, 'встречается чаще всего,', max_cnt, 'раз(а)')
else:
    print('все числа в массиве уникальны')
