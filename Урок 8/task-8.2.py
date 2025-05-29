n = int(input('Введите количество чисел для ввода: '))

while True:
    arr = list(map(int, input('Введите числа через пробел: ').split()))
    len_arr = len(arr)
    if len_arr < n:
        print(f"Вы ввели недостаточно чисел ({len_arr}), требуется {n}, повторите ввод.")
        continue
    elif len_arr > n:
        arr = arr[:n]        
        print(f"Вы ввели больше чем необходимо, список будет урезан до {n} чисел: {arr}")
    break


if n > 1:
    last = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last

# Вывод
print(' '.join(map(str, arr)))