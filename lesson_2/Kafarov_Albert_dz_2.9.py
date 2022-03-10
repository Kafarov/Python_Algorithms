# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


sum_num = 0
num = 0


while True:
    a = input('Введите натуральное число: ')
    if a == '0':
        print(f'Наибольшая сумма цифр у число {num} сумма цифр = {sum_num}')
        break
    else:
        summ = 0
        for i in a:
            summ += int(i)
        if summ > sum_num:
            sum_num = summ
            num = a
