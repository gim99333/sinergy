import collections

# База данных питомцев, для примера с двумя какими-то сущностями
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    """Функция для определения правильного склонения слова 'год'"""
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

def get_pet(ID):
    """Функция для получения информации о питомце по ID"""
    return pets[ID] if ID in pets else None

def pets_list():
    """Функция для отображения всего списка питомцев"""
    for ID, pet_info in pets.items():
        pet_name = list(pet_info.keys())[0]
        info = pet_info[pet_name]
        print(f"ID: {ID}")
        print(f'Это {info["Вид питомца"]} по кличке "{pet_name}". '
              f'Возраст питомца: {info["Возраст питомца"]} '
              f'{get_suffix(info["Возраст питомца"])}. '
              f'Имя владельца: {info["Имя владельца"]}')
        print()

def create():
    """Функция для создания новой записи о питомце"""
    last = collections.deque(pets, maxlen=1)[0]  # максимальное значение ключа в словаре
    new_id = last + 1
    
    pet_name = input('Введите кличку питомца: ')
    animal = input('Введите вид питомца: ')
    
    while True:
        try:
            age = int(input('Введите возраст питомца: '))
            if age < 0:
                print("Возраст не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Ошибка: нужно ввести целое число!")
    
    owner = input('Введите имя владельца: ')
    
    pets[new_id] = {
        pet_name: {
            "Вид питомца": animal,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Запись добавлена под ID: {new_id}")

def read(ID):
    """Функция для чтения информации о питомце"""
    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден")
        return
    
    pet_name = list(pet_info.keys())[0]
    info = pet_info[pet_name]
    print(f'Это {info["Вид питомца"]} по кличке "{pet_name}". '
          f'Возраст питомца: {info["Возраст питомца"]} '
          f'{get_suffix(info["Возраст питомца"])}. '
          f'Имя владельца: {info["Имя владельца"]}')

def update(ID):
    """Функция для обновления информации о питомце"""
    pet_info = get_pet(ID)
    if not pet_info:
        print(f"Питомец с ID {ID} не найден")
        return
    
    pet_name = list(pet_info.keys())[0]
    info = pet_info[pet_name]
    
    print("Текущая информация:")
    read(ID)
    print("\nВведите новые данные (оставьте пустым, чтобы не изменять):")
    
    new_name = input(f'Кличка питомца [{pet_name}]: ') or pet_name
    new_animal = input(f'Вид питомца [{info["Вид питомца"]}]: ') or info["Вид питомца"]
    
    while True:
        new_age = input(f'Возраст питомца [{info["Возраст питомца"]}]: ')
        if not new_age:
            new_age = info["Возраст питомца"]
            break
        try:
            new_age = int(new_age)
            if new_age < 0:
                print("Возраст не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Ошибка: нужно ввести целое число!")
    
    new_owner = input(f'Имя владельца [{info["Имя владельца"]}]: ') or info["Имя владельца"]
    
    # Обновляем данные
    del pets[ID][pet_name]
    pets[ID][new_name] = {
        "Вид питомца": new_animal,
        "Возраст питомца": new_age,
        "Имя владельца": new_owner
    }
    print("Данные обновлены!")

def delete(ID):
    """Функция для удаления записи о питомце"""
    if ID not in pets:
        print(f"Питомец с ID {ID} не найден")
        return
    
    pet_name = list(pets[ID].keys())[0]
    del pets[ID]
    print(f"Питомец {pet_name} (ID: {ID}) удален из базы данных")

# Основной цикл программы
def main():
    while True:
        print("\nДоступные команды: create, read, update, delete, list, stop")
        command = input("Введите команду: ").lower()
        
        if command == 'stop':
            break
        elif command == 'create':
            create()
        elif command == 'read':
            try:
                ID = int(input("Введите ID питомца: "))
                read(ID)
            except ValueError:
                print("Ошибка: ID должен быть числом!")
        elif command == 'update':
            try:
                ID = int(input("Введите ID питомца для обновления: "))
                update(ID)
            except ValueError:
                print("Ошибка: ID должен быть числом!")
        elif command == 'delete':
            try:
                ID = int(input("Введите ID питомца для удаления: "))
                delete(ID)
            except ValueError:
                print("Ошибка: ID должен быть числом!")
        elif command == 'list':
            pets_list()
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()