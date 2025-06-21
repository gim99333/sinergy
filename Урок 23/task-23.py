import pygame
import random
import time
import os
import json
from enum import Enum

# Инициализация pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
FPS = 10 # Размер тика - скорость игры
HEALTH = 6 # Здоровье - типа сколько тиков над горящим деревом можно летать до потери жизни

# Цвета (используются как fallback, если изображения не найдены)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LIGHT_BLUE = (135, 206, 250)

# Состояния клеток
class CellState(Enum):
    EMPTY = 0
    TREE = 1
    BURNING_TREE = 2
    BURNT_TREE = 3
    WATER = 4
    HOSPITAL = 5
    SHOP = 6

# Направления движения
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

# Погодные условия
class Weather(Enum):
    CLEAR = 0
    RAIN = 1
    THUNDERSTORM = 2

class HelicopterGame:   # Класс! 
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Вертолет-пожарный")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 20)
        
        # Игровое поле
        self.grid = [[CellState.EMPTY for _ in range(width)] for _ in range(height)]
        
        # Параметры игры
        self.score = 0
        self.helicopter_lives = 3
        self.water_capacity = 1
        self.max_water_capacity = 3
        self.helicopter_pos = [width // 2, height // 2]
        self.helicopter_direction = Direction.RIGHT
        self.game_over = False
        self.paused = False
        self.weather = Weather.CLEAR
        self.weather_duration = 0
        self.tick_count = 0
        
        # Время между событиями (в тиках)
        self.tree_growth_rate = 50
        self.fire_spread_rate = 30
        self.weather_change_rate = 200
        self.health = HEALTH  
        
        # Генерация карты
        self.generate_waters()
        self.generate_trees()
        self.generate_special_buildings()
        
        # Загрузка изображений
        self.load_images()
    
    def load_images(self):
        """Загружаем изображения или создаем цветные поверхности"""
        self.images = {}
        self.use_colors = False
        
        try:
            self.images[CellState.EMPTY] = pygame.Surface((CELL_SIZE, CELL_SIZE))
            self.images[CellState.EMPTY].fill(WHITE)
            
            # Пытаемся загрузить изображения из файлов
            image_files = {
                CellState.TREE: "tree.jpg",
                CellState.BURNING_TREE: "burning_tree.jpg",
                CellState.BURNT_TREE: "burnt_tree.jpg",
                CellState.WATER: "water.jpg",
                CellState.HOSPITAL: "hospital.jpg",
                CellState.SHOP: "shop.jpg"
            }
            
            for state, filename in image_files.items():
                if os.path.exists(filename):
                    img = pygame.image.load(filename)
                    self.images[state] = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
                else:
                    # Создаем цветную поверхность, если файл не найден
                    color = WHITE
                    if state == CellState.TREE:
                        color = GREEN
                    elif state == CellState.BURNING_TREE:
                        color = RED
                    elif state == CellState.BURNT_TREE:
                        color = BROWN
                    elif state == CellState.WATER:
                        color = BLUE
                    elif state == CellState.HOSPITAL:
                        color = YELLOW
                    elif state == CellState.SHOP:
                        color = GRAY
                    
                    self.images[state] = pygame.Surface((CELL_SIZE, CELL_SIZE))
                    self.images[state].fill(color)
            
            # Изображение вертолета
            if os.path.exists("helicopter.jpg"):
                self.helicopter_img = pygame.image.load("helicopter.jpg")
                self.helicopter_img = pygame.transform.scale(self.helicopter_img, (CELL_SIZE, CELL_SIZE))
            else:
                self.helicopter_img = pygame.Surface((CELL_SIZE, CELL_SIZE))
                self.helicopter_img.fill(BLACK)
            
        except Exception as e:
            print(f"Ошибка загрузки изображений: {e}")
            self.use_colors = True
    
    def generate_waters(self):
        """Генерация рек (вертикальных и горизонтальных)"""
        for i in range(self.height):
            if random.random() < 0.2:
                for j in range(self.width):
                    self.grid[i][j] = CellState.WATER
        
        for j in range(self.width):
            if random.random() < 0.2:
                for i in range(self.height):
                    self.grid[i][j] = CellState.WATER
    
    def generate_trees(self):
        """Генерация деревьев"""
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == CellState.EMPTY and random.random() < 0.3:
                    self.grid[i][j] = CellState.TREE
    
    def generate_special_buildings(self):
        """Генерация больницы и магазина"""
        empty_cells = []
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == CellState.EMPTY:
                    empty_cells.append((i, j))
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = CellState.HOSPITAL
            empty_cells.remove((i, j))
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = CellState.SHOP
    
    def is_valid_position(self, x, y):
        """Проверка корректности координат"""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def grow_trees(self):
        """Рост новых деревьев"""
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == CellState.EMPTY and random.random() < 0.01:
                    self.grid[i][j] = CellState.TREE
    
    def start_fires(self):
        """Начало пожаров"""
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == CellState.TREE and random.random() < 0.005:
                    self.grid[i][j] = CellState.BURNING_TREE
    
    def spread_fires(self):
        """Распространение пожаров"""
        new_fires = []
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == CellState.BURNING_TREE:
                    # Проверяем соседние клетки
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if self.is_valid_position(nj, ni) and self.grid[ni][nj] == CellState.TREE:
                            if random.random() < 0.3:
                                new_fires.append((ni, nj))
        
        for i, j in new_fires:
            self.grid[i][j] = CellState.BURNING_TREE
    
    def update_burning_trees(self):
        """Обновление сгорящих деревьев"""
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == CellState.BURNING_TREE:
                    if random.random() < 0.1:
                        self.grid[i][j] = CellState.BURNT_TREE
                        self.score -= 10  # Штраф за сгоревшее дерево
    
    def change_weather(self):
        """Смена погоды"""
        if self.weather_duration <= 0:
            weather_previous = self.weather
            while self.weather== weather_previous:
                self.weather = random.choice(list(Weather)) # Выбираем случайную погоду не равную прежней
            self.weather_duration = random.randint(30, 60)
        else:
            self.weather_duration -= 1
        
        # Эффекты погоды
        if self.weather == Weather.RAIN:
            # Дождь может тушить пожары
            for i in range(self.height):
                for j in range(self.width):
                    if self.grid[i][j] == CellState.BURNING_TREE and random.random() < 0.05:
                        self.grid[i][j] = CellState.TREE
                        self.score += 5  # Бонус за дождь, потушивший пожар
        elif self.weather == Weather.THUNDERSTORM:
            # Гроза может вызывать новые пожары
            if random.random() < 0.02:
                self.start_fires()
    
    def handle_input(self):
        """обработка нажатий стрелок"""
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[pygame.K_UP]:
            dy = -1
            self.helicopter_direction = Direction.UP
        elif keys[pygame.K_DOWN]:
            dy = 1
            self.helicopter_direction = Direction.DOWN
        elif keys[pygame.K_LEFT]:
            dx = -1
            self.helicopter_direction = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            dx = 1
            self.helicopter_direction = Direction.RIGHT
        
        # Движение вертолета
        new_x = self.helicopter_pos[0] + dx
        new_y = self.helicopter_pos[1] + dy
        
        if self.is_valid_position(new_x, new_y):
            self.helicopter_pos[0] = new_x
            self.helicopter_pos[1] = new_y
    
    def interact(self):
        """Взаимодействие с клеткой"""
        x, y = self.helicopter_pos
        cell = self.grid[y][x]
        
        if cell == CellState.WATER:
            # Набираем воду
            self.water_capacity = self.max_water_capacity
        elif cell == CellState.BURNING_TREE and self.water_capacity > 0:
            # Тушим пожар
            self.grid[y][x] = CellState.TREE
            self.water_capacity -= 1
            self.score += 20  # Бонус за тушение пожара
        elif cell == CellState.HOSPITAL:
            # Лечение в больнице если есть 50 баксов
            if self.helicopter_lives < 3 and self.score >= 50:
                self.helicopter_lives += 1
                self.health = HEALTH
                self.score -= 50
        elif cell == CellState.SHOP:
            # Улучшение в магазине
            if self.max_water_capacity < 5 and self.score >= 100:
                self.max_water_capacity += 1
                self.score -= 100
    
    def update(self):
        """Обновления событий по ходу игры"""
        if self.paused or self.game_over:
            return
        
        self.tick_count += 1
        self.weather_duration -=1

        # Обработка ввода
        self.handle_input()
        
        # Потеря здоровья и жизни при задержке над горящим деревом
        x, y = self.helicopter_pos
        if self.grid[y][x] == CellState.BURNING_TREE:
            self.health -= 1
            if self.health <= 0:
                self.helicopter_lives -= 1
                self.health = 0
                if self.helicopter_lives <= 0:
                    self.game_over = True

        # Периодические события
        if self.tick_count % self.tree_growth_rate == 0:
            self.grow_trees()
        
        if self.tick_count % self.fire_spread_rate == 0:
            self.start_fires()
            self.spread_fires()
            self.update_burning_trees()
        
        if self.tick_count % self.weather_change_rate == 0:
            self.change_weather()
    
    def draw(self):
        """Отрисовка элементов игрф"""
        self.screen.fill(WHITE)
        
        # Рисуем сетку
        for i in range(self.height):
            for j in range(self.width):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                # Рисуем клетку
                if self.use_colors:
                    color = WHITE
                    if self.grid[i][j] == CellState.TREE:
                        color = GREEN
                    elif self.grid[i][j] == CellState.BURNING_TREE:
                        color = RED
                    elif self.grid[i][j] == CellState.BURNT_TREE:
                        color = BROWN
                    elif self.grid[i][j] == CellState.WATER:
                        color = BLUE
                    elif self.grid[i][j] == CellState.HOSPITAL:
                        color = YELLOW
                    elif self.grid[i][j] == CellState.SHOP:
                        color = GRAY
                    
                    pygame.draw.rect(self.screen, color, rect)
                    pygame.draw.rect(self.screen, BLACK, rect, 1)
                else:
                    # Рисуем изображение
                    img = self.images.get(self.grid[i][j], None)
                    if img:
                        self.screen.blit(img, rect)
                    pygame.draw.rect(self.screen, BLACK, rect, 1)
        
        # Рисуем вертолет
        heli_x, heli_y = self.helicopter_pos
        heli_rect = pygame.Rect(heli_x * CELL_SIZE, heli_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        
        if not self.use_colors and hasattr(self, 'helicopter_img'):
            self.screen.blit(self.helicopter_img, heli_rect)
        else:
            pygame.draw.rect(self.screen, BLACK, heli_rect)
        
        # Рисуем погоду
        if self.weather == Weather.RAIN:
            for _ in range(20):
                x = random.randint(0, SCREEN_WIDTH)
                y = random.randint(0, SCREEN_HEIGHT)
                pygame.draw.line(self.screen, LIGHT_BLUE, (x, y), (x, y+5), 3)
        elif self.weather == Weather.THUNDERSTORM:
            self.screen.fill((50, 50, 50), special_flags=pygame.BLEND_MULT)
            if random.random() < 0.05:
                self.screen.fill(WHITE, special_flags=pygame.BLEND_ADD)
        
        # Рисуем UI
        score_text = self.font.render(f"Очки: {self.score}", True, BLACK)
        lives_text = self.font.render(f"Жизни: {self.helicopter_lives}", True, BLACK)
        water_text = self.font.render(f"Вода: {self.water_capacity}/{self.max_water_capacity}", True, BLACK)
        weather_text = self.font.render(f"Погода: {self.weather.name}", True, BLACK)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))
        self.screen.blit(water_text, (10, 70))
        self.screen.blit(weather_text, (10, 100))
        
        if self.paused:
            pause_text = self.font.render("ПАУЗА", True, RED)
            self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 10))
        
        if self.game_over:
            game_over_text = self.font.render("ИГРА ОКОНЧЕНА", True, RED)
            restart_text = self.font.render("Нажмите R для перезапуска", True, BLACK)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 20))
            self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 10))
        
        pygame.display.flip()
    
    def save_game(self, filename):
        """Сохранение игры"""
        data = {
            'width': self.width,
            'height': self.height,
            'grid': [[cell.value for cell in row] for row in self.grid],
            'score': self.score,
            'helicopter_lives': self.helicopter_lives,
            'water_capacity': self.water_capacity,
            'max_water_capacity': self.max_water_capacity,
            'helicopter_pos': self.helicopter_pos,
            'weather': self.weather.value,
            'weather_duration': self.weather_duration,
            'tick_count': self.tick_count
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    def load_game(self, filename):
        """Загрузка игры"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.width = data['width']
            self.height = data['height']
            self.grid = [[CellState(cell) for cell in row] for row in data['grid']]
            self.score = data['score']
            self.helicopter_lives = data['helicopter_lives']
            self.water_capacity = data['water_capacity']
            self.max_water_capacity = data['max_water_capacity']
            self.helicopter_pos = data['helicopter_pos']
            self.weather = Weather(data['weather'])
            self.weather_duration = data['weather_duration']
            self.tick_count = data['tick_count']
            self.game_over = False
            self.paused = False
            
            return True
        except:
            return False
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # выход по эскейр
                        running = False
                    elif event.key == pygame.K_p:   # пауза
                        self.paused = not self.paused
                    elif event.key == pygame.K_SPACE and not self.paused and not self.game_over:
                        self.interact() # дейстиве
                    elif event.key == pygame.K_r and self.game_over:
                        self.__init__(self.width, self.height)  # Перезапуск игры
                    elif event.key == pygame.K_s:   # сохранение игры
                        self.save_game('savegame.json')
                    elif event.key == pygame.K_l:    #загрузка сохраненной
                        self.load_game('savegame.json')
            
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()

# Запуск игры
if __name__ == "__main__":
    print("Добро пожаловать в игру 'Вертолет-пожарный'!")
    print("Управление:")
    print("Стрелки - движение вертолета")
    print("Пробел - взаимодействие с клеткой (набор воды, тушение пожара)")
    print("P - пауза")
    print("S - сохранить игру")
    print("L - загрузить игру")
    print("R - перезапуск после окончания игры")
    print("ESC - выход")
    
    width = int(input("Введите ширину поля (рекомендуется 20): ") or 20)
    height = int(input("Введите высоту поля (рекомендуется 15): ") or 15)
    
    game = HelicopterGame(width, height)
    game.run()