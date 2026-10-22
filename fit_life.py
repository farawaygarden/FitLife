# Проект FitLife - MVP версия 1.0

# Приветствие помощника, описание работы
print('Привет! 🙋')
print('Меня зовут Иван. Как жизнь?')
print()
print('Я твой интерактивный помощник и советник в FitLife.')
print('Сейчас я могу посчитать для тебя:')
print('1. индекс массы тела\n2. норму потребления воды')
print()

# Ввод и проверка имени пользователя
while True:
    user_name = input('Как тебя зовут? ')

    if user_name.isalpha() and not user_name.isascii():
        print(f'Очень рад, {user_name}!')
        break
    else:
        print('Введи другое имя')

# Проверям возраст пользователя
while True:
    user_age = int(input('Сколько тебе полных лет? '))

    try:
        if user_age < 18 or user_age > 130:
            print('❌ Наша программа не рассчитана на твой возраст')
            exit()
        else:
            print('Записал, спасибо!')
            break
    except ValueError:
        print('❌ Введи целое число')

# Проверяем допустимость значения веса пользователя
while True:
    user_weight = float(input('Скажи, пожалуйста, свой вес (кг): '))

    try:
        if user_weight < 10 or user_weight > 200:
            print('❌ Наша программа не рассчитана на твой вес')
            exit()
        else:
            print('Спасибо, записал!')
            break
    except ValueError:
        print('Пожалуйста, введи число в формате "31.8"')

# Проверяем допустимые параметры роста пользователя
while True:
    user_height = float(input('Скажи свой рост в метрах (например, 1.6): '))

    try:
        if user_height < 0.3 or user_height > 3:
            print('❌ Наша программа не рассчитана на твой рост')
            exit()
        else:
            print('Спасибо! Все параметры получены, готов посчитать')
            break
    except ValueError:
        print('Пожалуйста, введи число в формате 1.8')


bmi = round(user_weight / (user_height ** 2), 1)

water_ml = round(user_weight * 30 / 1000, 2)

print(f'Отчет для пользователя {user_name} ({user_age} лет)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма потребления воды: {water_ml} л. в день')
print()
print('Обращайся еще! ✅')
