
def parrents(age):
    if 2 <= age <= 6:
        answer = 'Иди в садик!'
    elif 0 <= age < 2:
        answer = 'Иди к мамке'
    elif 6 < age <= 17:
        answer = 'Иди в школу'
    elif 17 < age <= 23:
        answer = 'Иди в Универ'
    elif 23 < age <= 65:
        answer = 'Иди на работу'
    elif 65 < age < 120:
        answer = 'Наслаждайся пенсией'
    else:
        answer = 'Столько не живут'
    return answer

age = int(input('age??\n'))

print(parrents(age))