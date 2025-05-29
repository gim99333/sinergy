n = int(input("Введите число N: "))
count_zero = 0

for _ in range(n):
    num = int(input("Введите число: "))
    if num == 0:
        count_zero += 1

print("Количество чисел, равных нулю:", count_zero)
