# 1) Определение количества различных подстрок с использованием хеш-функции. 
# Пусть на вход функции дана строка. 
# Требуется вернуть количество различных подстрок в этой строке.

import hashlib


def amount_substring_in_string(a):
    
    substring_lst = []
    chunk = 1
    
    while chunk != len(a):
        for i in range(len(a) - chunk + 1):
            h_sub = hashlib.sha1(a[i:i+chunk].encode('utf-8')).hexdigest()
            
            if h_sub not in substring_lst:
                substring_lst.append(h_sub)
                
        chunk += 1
    
    return len(substring_lst)


print(amount_substring_in_string('papa'))
print(amount_substring_in_string('sova'))
print(amount_substring_in_string('beep boop beer!'))
