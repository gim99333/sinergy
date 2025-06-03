class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


# Создаем объект Autobus
bus = Autobus(name="Renaul Logan", max_speed=180, mileage=12)

# Выводим информацию о вместимости
print(bus.seating_capacity())


### ! Более компактный вариант, но он не использует код родительского класса через super() и нарушает принцип Don't Repeat Yourself:
class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"