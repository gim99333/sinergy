def factorial(n):
    """Вычисляет факториал числа n"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_sequence(n):
    """Создание списка факториалов от факториала n до 1"""
    initial_fact = factorial(n)
    fact_list = []
    
    for num in range(n, 0, -1):
        fact_list.append(factorial(num))
    
    return fact_list

# По заданию
number = int(input("Введите натуральное число: ")) # вводим 3
factorial_value = factorial(number)
result_list = factorial_sequence(factorial_value)
print(f"Факториал числа {number}: {factorial_value}")
print(f"Список факториалов: {result_list}")

### Задание можно трактовать двояко, то ли ввод 3 - это само задание, то ли как пример, и вводить можно что угодно
### Поэтому решение универсальное