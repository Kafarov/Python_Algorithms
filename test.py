# Задачка из 2 вебинара

def func(a, b):
    i = [str(i) for i in range(a, b+1)]
    st = i[0]
    a += 1
    return f'"{st}", ' + func(a, b) if len(i) > 1 else f'"{st}"'


# print(func(1, 5))


import random
from timeit import timeit
SIZE_1 = 10
SIZE_2 = 100
SIZE_3 = 1000
SIZE_4 = 10000

MIN_ITEM = 0
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
# array_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
# array_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]
# array_4 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_4)]


def max_cnt_num_2(array):
    num = max(array, key=array.count)
    return num 

# s = input().split()
# print(max(s, key=s.count))
# print(type(s))
# print(s)
# print(max_cnt_num_2(array_1))

def is_simple_num_2(num):     # or def prime_num() не знаю как правильно
    if num == 2:
        return 1
    cnt = 1
    check_num = 3
    simple_num_lst = [2]
    while cnt != num:
        for i in simple_num_lst:
            if check_num % i == 0:
                check_num += 2
                break
        else:
            cnt += 1
            simple_num_lst.append(check_num)
            check_num += 2
    
    return check_num - 2

i = int(input('Введите порядковый номер искомого простого числа: '))
print(is_simple_num_2(i))