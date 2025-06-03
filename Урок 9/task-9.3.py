numbers = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
yes = set()
for num in numbers:
    if num in yes:
        print(num, "YES")
    else:
        print(num, "NO")
        yes.add(num)