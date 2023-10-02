# Просимо користувача ввести рядок
input_string = input("Введіть рядок символів: ")

# Створюємо пустий словник для зберігання частоти символів
character_frequency = {}

# Перебираємо всі символи у введеному рядку
for char in input_string:
    # Використовуємо метод count() для підрахунку кількості входжень символу
    frequency = input_string.count(char)
    # Зберігаємо частоту в словнику
    character_frequency[char] = frequency

# Виводимо результати
print("Частота зустрічі символів у введеному рядку:")
for char, frequency in character_frequency.items():
    print(f"'{char}': {frequency}")
