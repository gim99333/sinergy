import random

def generate_matrix(rows, cols):
    """Генерирует матрицу заданного размера со случайными значениями от -100 до 100"""
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix, name):
    """Выводит матрицу на экран с указанием имени"""
    print(f"\nМатрица {name}:")
    for row in matrix:
        print(' '.join(f'{num:4}' for num in row))

def add_matrices(matrix1, matrix2):
    """Складывает две матрицы одинакового размера"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинакового размера для сложения")
    
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] 
        for i in range(len(matrix1))
    ]

# Ввод параметров матриц
rows = int(input("Введите количество строк матриц: "))
cols = int(input("Введите количество столбцов матриц: "))

# Генерация матриц
matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

# Сложение матриц
matrix_3 = add_matrices(matrix_1, matrix_2)

# Вывод результатов
print_matrix(matrix_1, "1")
print_matrix(matrix_2, "2")
print_matrix(matrix_3, "3 (результат сложения)")