# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

num1 = int(input("Введите целое число: "))
num2 = 0

while num1 > 0:
    digit = num1 % 10
    num1 //= 10
    num2 *= 10
    num2 += digit

print('"Обратное" ему число:', num2)
