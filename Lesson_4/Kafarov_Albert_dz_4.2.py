# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

# Второй — без использования «Решета Эратосфена».

import cProfile
from timeit import timeit


# Способ 1. «Решето Эратосфена»

# Сложность примерно O(n). Память O(n)
def eratosfen_def(n, list_len=10_000):
    lst = [i for i in range(list_len+1)]
    lst[1] = 0
    m = 2
    while m < list_len**0.5:        # Дальше смотреть смысла нет
        if lst[m] != 0:
            j = m ** 2              # Известные закономерности
            while j <= list_len:
                lst[j] = 0
                j = j + m
        m += 1
    finish_lst = [i for i in lst if lst[i] != 0]
    del lst
    return finish_lst[n] 


# Ничего лучше не придумал
# n = int(input("Введите порядковый номер искомого простого числа:"))
# if n < 168:
#     print(eratosfen_def(n, 1000))
# elif n < 1229:
#     print(eratosfen_def(n, 10000))
# elif n < 10000:
#     print(eratosfen_def(n, 104729))
# else:
#     print(f'Значение за границами вычислений')

print('Вывод способа 1. "Решето Эратосфена"\n')
print(timeit('eratosfen_def(21, 100)', globals=globals(), number=1000))         # 0.04692919994704425
print(timeit('eratosfen_def(75, 1000)', globals=globals(), number=1000))        # 0.4145286000566557
print(timeit('eratosfen_def(75, 10000)', globals=globals(), number=1000))       # 3.5405663000419736
print(timeit('eratosfen_def(75, 100000)', globals=globals(), number=1000))      # 41.27304859994911

cProfile.run('eratosfen_def(75, 100000)')
'''         6 function calls in 0.066 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.066    0.066 <string>:1(<module>)
        1    0.049    0.049    0.065    0.065 Kafarov_Albert_dz_4.2.py:18(eratosfen_def)
        1    0.006    0.006    0.006    0.006 Kafarov_Albert_dz_4.2.py:19(<listcomp>)
        1    0.010    0.010    0.010    0.010 Kafarov_Albert_dz_4.2.py:29(<listcomp>)
        1    0.000    0.000    0.066    0.066 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''



# Способ 2. Метод перебором в "лоб"
# сложность видимо O(2**n)
def is_simple_num(num):     # or def prime_num() не знаю как правильно
    if num == 2:
        return 1
    cnt = 1
    check_num = 3
    while cnt != num:
        n = 2
        while n <= check_num:
            if n == check_num:
                cnt += 1
                check_num += 2
                break
            if check_num % n == 0:
                check_num += 2
                n = 2
                break
            else:
                n += 1
    
    return check_num - 2



# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(is_simple_num(i))

print('Вывод способа 2.\n')
# Порядковый номер выбрал так, чтобы количество перебираемых значений росло линейно
print(timeit('is_simple_num(26)', globals=globals(), number=1000))      # 0.13348219997715205
print(timeit('is_simple_num(168)', globals=globals(), number=1000))     # 12.35385270009283
# print(timeit('is_simple_num(1229)', globals=globals(), number=1000))  # 1005.9087550000986
# print(timeit('is_simple_num(9590)', globals=globals(), number=1000))  # Слишком долго
cProfile.run('is_simple_num(168)')
'''         4 function calls in 0.022 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.022    0.022 <string>:1(<module>)
        1    0.022    0.022    0.022    0.022 Kafarov_Albert_dz_4.2.py:67(is_simple_num)
        1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''
        

# Способ 3. Улучшим 2й способ, добавив дополнительный массив с простыми числами, 
# если искомое число не делится на все предшевствующие простые числа то он простой.
# Это Можно отнести к «Решето Эратосфена»? Принцип тот же
# Сложность O(n**2). Гораздо выше чем у способа №1
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

# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(is_simple_num_2(i))


print('Вывод способа 3.\n')
# Порядковый номер выбрал так, чтобы количество перебираемых значений росло линейно
print(timeit('is_simple_num_2(26)', globals=globals(), number=1000))      # 0.061497599934227765
print(timeit('is_simple_num_2(168)', globals=globals(), number=1000))     # 1.162032900028862
print(timeit('is_simple_num_2(1229)', globals=globals(), number=1000))    # 60.08326870005112
# print(timeit('is_simple_num_2(9590)', globals=globals(), number=1000))  # Слишком долго
cProfile.run('is_simple_num_2(1000)')
'''         1003 function calls in 0.085 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.085    0.085 <string>:1(<module>)
        1    0.085    0.085    0.085    0.085 Kafarov_Albert_dz_4.2.py:114(is_simple_num_2)
        1    0.000    0.000    0.085    0.085 {built-in method builtins.exec}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''
