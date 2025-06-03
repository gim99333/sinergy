class Turtle:
    def __init__(self, x=0, y=0, s=1):
        """Инициализация черепашки с позицией (x, y) и шагом s"""
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        """Увеличивает y на s"""
        self.y += self.s
    
    def go_down(self):
        """Уменьшает y на s"""
        self.y -= self.s
    
    def go_left(self):
        """Уменьшает x на s"""
        self.x -= self.s
    
    def go_right(self):
        """Увеличивает x на s"""
        self.x += self.s
    
    def evolve(self):
        """Увеличивает шаг s на 1"""
        self.s += 1
    
    def degrade(self):
        """Уменьшает шаг s на 1 с проверкой"""
        if self.s <= 1:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.s -= 1
    
    def count_moves(self, x2, y2):
        """Вычисляет минимальное количество ходов до точки (x2, y2)"""
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        # Вычисляем количество шагов по каждой оси
        moves_x = dx // self.s
        moves_y = dy // self.s
        
        # Остатки после полных шагов
        remainder_x = dx % self.s
        remainder_y = dy % self.s
        
        # Если остатки есть, потребуется дополнительный шаг
        total_moves = moves_x + moves_y
        if remainder_x != 0 or remainder_y != 0:
            total_moves += 1
        
        return total_moves
    
    def __str__(self):
        """Строковое представление черепашки"""
        return f"Черепашка в позиции ({self.x}, {self.y}) с шагом {self.s}"


# Для примера
if __name__ == "__main__":
    t = Turtle(0, 0, 2)  # Создаем черепашку в (0, 0) с шагом 2
    
    print(t)  # Черепашка в позиции (0, 0) с шагом 2
    
    t.go_up()
    t.go_right()
    print(t)  # Черепашка в позиции (2, 2) с шагом 2
    
    t.evolve()
    print(f"Шаг увеличен: {t.s}")  # 3
    
    t.go_down()
    t.go_left()
    print(t)  # Черепашка в позиции (-1, -1) с шагом 3
    
    try:
        t.degrade()
        t.degrade()
        t.degrade()  # Вызовет ошибку
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ошибка: Шаг не может быть меньше или равен 0
    
    print(f"Минимальное число ходов до (5, 5): {t.count_moves(5, 5)}")  # 2