n = int(input('Введите количество чисел N:'))
numbers = list(map(int, input(f"Введите {n} чисел через пробел:").split()))
unique_numbers = set(numbers)
print('Количесвто уникальных чисел в веденном наборе: ', len(unique_numbers))