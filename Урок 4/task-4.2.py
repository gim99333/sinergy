number = int(input("Введите пятизначное число: "))

# Разбиваем число на цифры
tens_of_thousands = number // 10000  # десятки тысяч
thousands = (number // 1000) % 10    # тысячи
hundreds = (number // 100) % 10      # сотни
tens = (number // 10) % 10           # десятки
units = number % 10                   # единицы

# Выполняем вычисления
step1 = tens ** units                # десятки в степени единиц
step2 = step1 * hundreds             # умножаем на сотни
denominator = tens_of_thousands - thousands  # разность дес.тыс. и тысяч

if denominator == 0:
    print("Ошибка: деление на ноль (разность десятков тысяч и тысяч равна нулю)")
else:
    result = step2 / denominator
    print(f"Результат: {result}")
