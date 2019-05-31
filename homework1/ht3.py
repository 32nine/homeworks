school_list = [
    # неправильное форматирование
                {'school_class': '1a', 'scores':[3,4,4,5,2]},
                {'school_class': '2a', 'scores':[5,4,4,5,5]},
                {'school_class': '3a', 'scores':[2,2,2,3,2]},
                ]



def school_cheker(school_class_numb):
    # ну такое, это не чистая функция, потому что неявно зависит от school_list
    # лучше было бы сразу передавать список оценок
    summary_scores = 0
    scores = school_list[school_class_numb]['scores']

    # не используй однубуквенные переменные для такого
    for i in scores:
        summary_scores = summary_scores + i

    av_summary_scores = summary_scores/len_shool_list

    return summary_scores

j = 0
total_sum = 0
len_shool_list = len(school_list)

а зачем через while?
while j < len_shool_list:
    numb = school_list[j]['school_class'] 
    # > Почему-то если сразу всталяю в шаблон ф-строки выдает ошибку синтаксиса
    # из-за ' символа
    print(f'Средний балл класса {numb} равен {school_cheker(j)}')
    total_sum = total_sum + school_cheker(j)
    j += 1


print(f'Средний балл по школе {total_sum}') # это сумма, а не средний балл
