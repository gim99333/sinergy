word = input("Введите слово из маленьких латинских букв: ").lower()

vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonant_count = 0

for letter in word:
    if letter in vowels:
        vowel_counts[letter] += 1
    elif letter.isalpha():
        consonant_count += 1

total_vowels = sum(vowel_counts.values())

print(f"Количество гласных:   {total_vowels}")
print(f"Количество согласных: {consonant_count}")

# Выводим количество каждой гласной или False, если её нет
for vowel, count in vowel_counts.items():
    if count > 0:
        print(f"Буква '{vowel}': {count} раз")
    else:
        print(f"Буква '{vowel}': False")