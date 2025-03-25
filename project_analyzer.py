import os

# Директории, которые нужно игнорировать
IGNORE_DIRS = {'venv', 'env', '.env', '.venv', 'node_modules', '.git', '__pycache__', '.idea'}


def print_project_structure(start_path):
    """
    Рекурсивно выводит структуру директорий и файлов в виде дерева.
    Возвращает список всех файлов для последующего вывода содержимого.
    """
    files_list = []

    def _print_tree(path, prefix='', is_last=False):
        """Вспомогательная функция для рекурсивного построения дерева"""
        try:
            entries = []
            for entry in os.listdir(path):
                if entry in IGNORE_DIRS:
                    continue
                full_path = os.path.join(path, entry)
                entries.append((entry, full_path, os.path.isdir(full_path)))

            # Сортируем директории перед файлами
            entries.sort(key=lambda x: (not x[2], x[0]))

            for i, (name, full_path, is_dir) in enumerate(entries):
                is_last_entry = i == len(entries) - 1
                connector = '└── ' if is_last_entry else '├── '

                if is_last:
                    new_prefix = prefix + '    '
                else:
                    new_prefix = prefix + '│   '

                print(f"{prefix}{connector}{name}")

                if is_dir:
                    _print_tree(full_path, new_prefix, is_last_entry)
                else:
                    files_list.append(full_path)
        except PermissionError:
            print(f"{prefix}└── [Ошибка доступа: {path}]")
        except Exception as e:
            print(f"{prefix}└── [Ошибка: {e}]")

    print(f"\nСтруктура проекта: {os.path.abspath(start_path)}\n")
    _print_tree(start_path)
    return files_list


def print_file_contents(files_list):
    """Выводит содержимое файлов с обработкой ошибок чтения"""
    print("\n\nСОДЕРЖИМОЕ ФАЙЛОВ:\n" + "=" * 50)
    for file_path in files_list:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"\nФайл: {file_path}\n{'-' * 40}")
                print(content)
        except UnicodeDecodeError:
            print(f"\nФайл: {file_path}\n{'-' * 40}\n[Бинарный файл или неподдерживаемая кодировка]")
        except Exception as e:
            print(f"\nФайл: {file_path}\n{'-' * 40}\n[Ошибка чтения: {str(e)}]")
        print("=" * 50)


if __name__ == "__main__":
    # Определяем корневую директорию проекта
    project_root = os.getcwd()  # Текущая директория (корень проекта в PyCharm)

    # Печатаем структуру и получаем список файлов
    file_list = print_project_structure(project_root)

    # Печатаем содержимое файлов
    print_file_contents(file_list)