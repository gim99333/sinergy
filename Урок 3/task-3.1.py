# Ввод вида животного
animal = input('Введите вид Вашего питомца: ')          

# Ввод возраста с проверкой, что введено целое числовое значение
while True:                                             
    age_input = input("Введите его возраст (лет): ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Ошибка: нужно ввести целое число!")

# Функция для определения названия года в зависимости от количества лет (год/года/лет)
def get_yearname(age):
    s = str(age)
    if (len(s)>1 and s[-2]=='1') or (s[-1] in '056789'):
        return 'лет'
    elif s[-1] == '1':
        return 'год'
    else:
        return 'года'

# Ввод клички
name = input('Введите его кличку:')                    

# Вывод результата
print(f'Это {animal} по кличке "{name}". Возраст: {age} {get_yearname(age)}.')
