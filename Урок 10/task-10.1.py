# Создаем пустой словарь
pets = {}

# Функция для определения названия года
def get_yearname(age):
    s = str(age)
    if (len(s) > 1 and s[-2] == '1') or (s[-1] in '056789'):
        return 'лет'
    elif s[-1] == '1':
        return 'год'
    else:
        return 'года'

# Ввод данных о питомце
name = input('Введите кличку питомца: ')
animal = input('Введите вид питомца: ')

# Ввод возраста с проверкой
while True:
    age_input = input('Введите возраст питомца: ')
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число!")

owner = input('Введите имя владельца: ')

# Добавляем информацию в словарь
pets[name] = {
    'Вид питомца': animal,
    'Возраст питомца': age,
    'Имя владельца': owner
}

# Получаем информацию о добавленном питомце
pet_info = pets[name]
year_word = get_yearname(pet_info['Возраст питомца'])

# Выводим результат
print(f'Это {pet_info["Вид питомца"]} по кличке "{name}". Возраст питомца: {pet_info["Возраст питомца"]} {year_word}. Имя владельца: {pet_info["Имя владельца"]}')