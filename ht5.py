one = input('Введите первое число: ')
two = input('Введите второе число: ')

def get_sum(one,two):
    try:
        result = int(one) + int(two)
        
    except ValueError:
        result = 'приведение типов не сработало'
    return result

print(get_sum(one,two))