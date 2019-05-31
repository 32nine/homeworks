# лучше сначала объявлять функции, а потом уже тело программы *
def get_sum(one,two):
    try:
        result = int(one) + int(two)
        
    except ValueError:
        result = 'приведение типов не сработало'
    return result

one = input('Введите первое число: ')
two = input('Введите второе число: ')

print(get_sum(one,two))
