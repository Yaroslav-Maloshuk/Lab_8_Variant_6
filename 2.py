# Просимо користувача ввести адресу файлу
file_path = input("Введіть адресу файлу (зі зворотніми слешами \\): ")

# Використовуємо метод split() для розбиття шляху на частини
path_parts = file_path.split("\\")

# Останній елемент розділеного шляху - назва файлу
file_name = path_parts[-1]

# Розділяємо назву файлу на назву та розширення
name_parts = file_name.split(".")

# Перевіряємо, чи є розширення (мінімум дві частини після розділення точкою)
if len(name_parts) > 1:
    file_extension = name_parts[-1]
else:
    file_extension = "Розширення відсутнє"

# Виводимо результати
print(f"Назва файлу: {name_parts[0]}")
print(f"Розширення файлу: {file_extension}")

