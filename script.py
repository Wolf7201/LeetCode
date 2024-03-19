import os
import re

# Получение текущей директории
directory_path = os.getcwd()

# Регулярное выражение для поиска файлов, начинающихся с числа и содержащих точки и пробелы
pattern = re.compile(r'(\d+)\.\s*(.+?)\.py')

# Проходим по всем файлам в директории
for filename in os.listdir(directory_path):
    if match := pattern.match(filename):
        # Извлекаем номер задачи и имя без начальных цифр, точек и пробелов
        problem_number, problem_name = match.groups()
        # Убираем пробелы и точки, заменяем их на нижние подчеркивания и приводим к нижнему регистру
        new_problem_name = problem_name.replace(' ', '_').replace('.', '_').lower()
        # Формируем новое имя файла
        new_filename = f'problem_{problem_number}_{new_problem_name}.py'
        # Полный путь к старому и новому файлам
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_filename)
        # Переименовываем файл
        os.rename(old_file_path, new_file_path)
        print(f'Renamed "{filename}" to "{new_filename}"')

print("Renaming complete.")
