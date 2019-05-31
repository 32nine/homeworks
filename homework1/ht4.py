
answers = {'как дела?':'Хорошо!','что делаешь?':'Программирую','куда пойти?':'На курсы Learn.Python конечно!'}

def ask_user(answers):
    # А вот ту ты явно передаешь константный словарь, не понятно зачем
    user_say = input('Что надо?\n')
    user_say = user_say.lower()
    result = answers.get(user_say)
    return result
    
try:
    while True:
        # try/except лучше начинать здесь, а не оборачивать всю программу
        answer = ask_user(answers)
        if answer == None:
            print('ты втираешь какую-то дичь!')
            break
        else:
            print(answer)
except KeyboardInterrupt:
    print('Пока!')

    
