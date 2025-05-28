# Официальные (нагугленные) этапы развития человека
protoantrops_data = [
'Дриопитек, рамапитек', 
'Австралопитек',
'Человек умелый (Homo habilis)',
'Человек прямоходящий (Homo erectus)',
'Человек гейдельбергский (Homo heidelbergensis)',
'Неандерталец (Homo neanderthalensis)',
'Человек разумный (Homo sapiens)',
'Человек современной анатомии (Homo sapiens sapiens)'
]

# Чтение в список вводимых этапов (не более 8)
protoantrops_input = []
i = 1
while True:
    stage = input(f"Введите {i}-й этап развития человека: ")
    if not stage:
        break
    protoantrops_input.append(stage)
    i += 1
    if i>8:
        print("Официальных этапов больше нет")
        break

# Вывод введенных этапов
print('\nЭтапы развития человека, введенные Вами: ')
print(*protoantrops_input, sep='=>')

# Вывод официальных этапов (для сравнения)
print('\nЭтапы развития человека официальные: ')
print(*protoantrops_data, sep='=>')