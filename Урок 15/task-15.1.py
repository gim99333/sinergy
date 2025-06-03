class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass  # Наследует все методы и атрибуты родительского класса

# Создаем объект Autobus
bus = Autobus(name="Renaul Logan", max_speed=180, mileage=12)

# Выводим информацию об объекте
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")