def process_log_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()  # Читаем все строки из файла
        ISMIS = 0  # Инициализируем счетчик ISMIS
        for line in lines:
            # Проверяем, содержит ли строка "is missing!"
            if "is missing!" in line:
                ISMIS += 1  # Увеличиваем счетчик ISMIS на 1
                # Считываем следующие 22 символа после "is missing!"
                index = line.index("is missing!")
                next_chars = line[index + 12:index + 34]
                print(f"Найдено 'is missing!': {next_chars}")

        print(f"Общее количество 'is missing!': {ISMIS}")