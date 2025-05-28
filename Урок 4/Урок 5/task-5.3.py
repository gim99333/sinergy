X = int(input("Введите минимальную сумму инвестиций X: "))
A = int(input("Количество долларов у Майкла: "))
B = int(input("Количество долларов у Ивана: "))

mike_can = A >= X
ivan_can = B >= X
both_can = mike_can and ivan_can
together_can = A + B >= X

if both_can:
    print(2)
elif mike_can:
    print("Mike")
elif ivan_can:
    print("Ivan")
elif together_can:
    print(1)
else:
    print(0)