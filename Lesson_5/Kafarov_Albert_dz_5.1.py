# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# Замучился с этой простой задачкой. не знал куда впихнуть коллекции чтоб это небыло костылем
# Делал вариант с именованным кортежем, убил кучу времени, не понравилась логика которую придумал - забросил
# Сдаю это не бейте сильно ногами=)
from collections import Counter


a = int(input('Введите количество предприятий: '))
cnt = 0
company_dict = {}

while cnt != a:
    b = input('Введите наименование предприятия и прибыль за 4 квартала, через пробел: ').split()
    company_dict[b[0]] = [int(_) for _ in b[1:]]
    cnt += 1


mean_profit_company = {key: sum(company_dict[key])/4 for key in company_dict}
mean_profit = sum(sum(company_dict[key]) for key in company_dict)/4/a


for key in Counter(mean_profit_company):
    if mean_profit_company[key] > mean_profit:
        print('У следующих компаний прибыль выше среднего', end='\n')
        print(f'Компания {key} имеет прибыль, {mean_profit_company[key]} у.е.')
    elif mean_profit_company[key] == mean_profit:
        print('У следующих компаний прибыль равна средней', end='\n')
        print(f'Компания {key} имеет прибыль {mean_profit_company[key]} у.е.')
    else:
        print('У следующих компаний прибыль ниже среднего', end='\n')
        print(f'Компания {key} имеет прибыль, {mean_profit_company[key]} у.е.')
