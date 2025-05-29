# Ввод A и B в одной строке через пробел
while True:
    A = int(input('Введите число А: '))
    B = int(input('Введите число В, больше чем А: '))
    if B > A:
        break
    else: 
        print(f"A={A} больше B={B}. Введите числа по условию А < B!")

# Находим первое чётное число >= A
ord_1 = A if A % 2 == 0 else A + 1

# Выводим чётные числа от ord1 до B с шагом 2
evens = range(ord_1, B + 1, 2)
print(' '.join(map(str, evens)))