# Проект FitLife - MVP версия 1.0

# приветствие и знакомство
def intro():
    """Приветствие помощника, описание работы"""
    print('Привет! 🙋')
    print('Меня зовут Иван. Как жизнь?')
    print()
    print('Я твой интерактивный помощник и советник.')
    print('Сейчас я могу посчитать для тебя:')
    print('1. индекс массы тела\n2. норму потребления воды')
    print()


# запрос и проверка имени
def name_check(name):
    """Проверка имени пользователя"""
    while True:
        input_name = input(name)

        if input_name.isalpha() and not input_name.isascii():
            print(f'Очень рад, {input_name}!')
            return input_name
        else:
            print('Введи другое имя')


def age_check(age):
    """Проверям возраст пользователя"""
    while True:
        input_age = int(input(age))

        try:
            if input_age < 18 or input_age > 130:
                print('❌ Наша программа не рассчитана на твой возраст')
                exit()
            else:
                print('Записал, спасибо!')
                return input_age
        except ValueError:
            print('❌ Введи целое число')


def weight_check(weight):
    """Проверяем допустимость значения веса пользователя"""
    while True:
        input_weight = float(input(weight))

        try:
            if input_weight < 10 or input_weight > 200:
                print('❌ Наша программа не рассчитана на твой вес')
                exit()
            else:
                print('Спасибо, записал!')
                return input_weight
        except ValueError:
            print('Пожалуйста, введи число в формате "31.8"')


def height_check(height):
    """Проверяем допустимые параметры роста пользователя"""
    while True:
        input_height = float(input(height))

        try:
            if input_height < 0.3 or input_height > 3:
                print('❌ Наша программа не рассчитана на твой рост')
                exit()
            else:
                print('Спасибо! Все параметры получены, готов посчитать')
                return input_height
        except ValueError:
            print('Пожалуйста, введи число в формате 1.8')


def calc_bmi(w, h):
    """Расчет индекса массы тела"""
    bmi = w / h ** 2
    bmi = round(bmi, 1)

    return bmi


def calc_water(w):
    """Расчет нормы потребления воды"""
    water_ml = w * 30
    water_ml = round(water_ml / 1000, 2)

    return water_ml


intro()

user_name = name_check('Как тебя зовут? ')

user_age = age_check('Сколько тебе полных лет? ')

user_weight = weight_check('Скажи, пожалуйста, свой вес (кг): ')

user_height = height_check('Скажи свой рост в метрах (например, 1.6): ')

bmi = calc_bmi(user_weight, user_height)

water_ml = calc_water(user_weight)

print(f'Отчет для пользователя: {user_name} ({user_age} лет)', flush=True)
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма потребления воды: {water_ml} л. в день')
print()
print('Обращайся еще! ✅')
