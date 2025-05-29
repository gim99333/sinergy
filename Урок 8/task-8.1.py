n = int(input('Введите количество чисел для последующего ввода: '))     # Читаем количество чисел

print(f"Введите {n} чисел подряд:")
numbers = [int(input()) for _ in range(n)]                              # Читаем числа в список

reversed_numbers = numbers[::-1]                                        # Переворачиваем список

print('\nСписок чисел наоброт:')
print('\n'.join(map(str, reversed_numbers)))                            # Выводим по одному числу в строке