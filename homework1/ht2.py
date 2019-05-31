def string_cheker(str1, str2):
    if type(str1) == str and type(str2) == str:
        # по заданию нужно возвращать 0
        answer = 'its string!\n'
        if str1 == str2:
            # можно сразу писать return 1 
            answer = 1
        if str1 > str2:
            answer = 2
        if str1 != str2 and str2 == 'learn':
            answer = 3
    else:
        answer = 0
    return answer
  
answer = 0 

# зачем тут while?
while answer < 3: # не могу понять почему не выходит из цикла, он как то забирает переменную answer = 0, хотя она вне тела цикла

    str1 = input('Введите строку 1\n')
    str2 = input('Введите строку 2\n')

    print(string_cheker(str1, str2))
