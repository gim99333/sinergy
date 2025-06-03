class CashRegister:
    def __init__(self, initial_amount=0):
        """Инициализация кассы с начальной суммой (по умолчанию 0)"""
        self.balance = initial_amount
    
    def top_up(self, x):
        """Пополняет кассу на указанную сумму"""
        if x < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной")
        self.balance += x
    
    def count_1000(self):
        """Возвращает количество целых тысяч в кассе"""
        return self.balance // 1000
    
    def take_away(self, x):
        """Извлекает указанную сумму из кассы"""
        if x < 0:
            raise ValueError("Сумма изъятия не может быть отрицательной")
        if x > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= x
    
    def __str__(self):
        """Строковое представление кассы"""
        return f"В кассе: {self.balance} руб. (целых тысяч: {self.count_1000()})"


# Пример применения класса
if __name__ == "__main__":
    kassa = CashRegister(5000)  # Создаем кассу с 5000 рублей
    
    print(kassa)  # В кассе: 5000 руб. (целых тысяч: 5)
    
    kassa.top_up(3000)  # Пополняем на 3000
    print(f"После пополнения: {kassa.balance}")  # 8000
    
    print(f"Целых тысяч: {kassa.count_1000()}")  # 8
    
    kassa.take_away(4500)  # Забираем 4500
    print(f"После изъятия: {kassa.balance}")  # 3500
    
    try:
        kassa.take_away(4000)  # Пытаемся забрать больше чем есть
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ошибка: Недостаточно денег в кассе