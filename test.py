# Задачка из 2 вебинара

def func(a, b):
    i = [str(i) for i in range(a, b+1)]
    st = i[0]
    a += 1
    return f'"{st}", ' + func(a, b) if len(i) > 1 else f'"{st}"'


print(func(1, 5))
