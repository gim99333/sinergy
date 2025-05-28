animal = input('Введите вид Вашего питомца: ')          # Ввод вида животного

while True:                                             # Ввод возраста с проверкой, что введено 
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

name = input('Введите его кличку:')                     # Ввод клички

# Вывод результата
print(f'Это {animal} по кличке "{name}". Возраст: {age} {get_yearname(age)}.')
