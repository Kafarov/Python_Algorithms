# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Решить эту задачу оказалось легче чем первую, для меня. Замучился писать словарь))
# К началу урока не успею попробовать сделать умножение. Но займусь этим позже, если успею до проверки обновлю ссылку на пул реквест
from collections import deque
from itertools import zip_longest


def hex_sum(a, b):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    source = list(zip_longest(a[::-1], b[::-1], fillvalue='0'))
    sum_res = deque()
    stack = 0
    for i in source:
        if stack:
            res = hex_dict[i[0]] + hex_dict[i[1]] + stack
            stack = 0
        else:
            res = hex_dict[i[0]] + hex_dict[i[1]]
        if res > 15:
            sum_res.appendleft(hex_dict[res - 16])
            stack += 1
        else:
            sum_res.appendleft(hex_dict[res])
    if stack:
        sum_res.appendleft(hex_dict[stack])
    return sum_res


a = [i for i in input('Введите первое число: ')]
b = [i for i in input('Введите второе число: ')]
print(a, b)

x = hex_sum(a, b)
print(x)
