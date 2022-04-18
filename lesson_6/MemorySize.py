import sys


def get_sizeof(x):
    size_sum = 0
    unique_id = set()
    
    for key, value in x.items():
        if key.startswith('__'):
            # убираем "магию"
            continue
        elif hasattr(value, '__call__'):
            # убираем функции
            continue
        elif hasattr(value, '__loader__'):
            # убираем модули
            continue
        elif id(value) in unique_id:
            # убираем объекты (переменные), которые уже попали в сумму
            continue
        else:
            
            if type(value) is str or type(value) is set:
                size_sum += sys.getsizeof(value)
                unique_id.add(id(value))
            elif hasattr(value, '__iter__'):
                if hasattr(value, 'items'):
                    for k, v in value.items():
                        # Если id значения а множестве уникальныых значений, суммируем только размер ключа
                        if id(v) in unique_id:
                            size_sum += sys.getsizeof(k)
                            continue                        
                        unique_id.add(id(v))
                        size_sum += sys.getsizeof(k)
                        size_sum += sys.getsizeof(v)
                else:
                    unique_id.add(id(value))
                    for xx in value:
                        if id(xx) in unique_id:
                            continue
                        size_sum += sys.getsizeof(xx)
                        unique_id.add(id(xx))
    
    return size_sum
