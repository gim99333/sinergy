num = int(input("Введите целое число: "))

if num == 0:
    print("нулевое число")
else:
    # Определяем знак числа
    if num > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"
    
    # Проверяем чётность
    parity = "четное" if num % 2 == 0 else 'нечетное'
        
    #Вывод
    print(f"{sign} {parity} число")
    if num % 2 != 0:
        print("число не является четным")