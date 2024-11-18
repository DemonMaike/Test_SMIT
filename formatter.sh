#!/bin/bash

# Проверяем, установлен ли Poetry
if ! command -v poetry &> /dev/null
then
    echo "Poetry не установлен. Установите его через 'pip install poetry'."
    exit 1
fi

# Проверяем, установлен ли autopep8 в виртуальном окружении Poetry
if ! poetry run autopep8 --version &> /dev/null
then
    echo "autopep8 не установлен в Poetry окружении. Установите его через 'poetry add --dev autopep8'."
    exit 1
fi

# Проверяем, переданы ли директории для обработки
if [ "$#" -eq 0 ]; then
    echo "Укажите хотя бы одну директорию для форматирования, например: ./poetry_format_all.sh app tests"
    exit 1
fi

echo "Форматируем файлы Python в следующих директориях: $* через Poetry"

# Проходим по указанным директориям
for DIR in "$@"
do
    if [ -d "$DIR" ]; then
        echo "Обрабатываем директорию: $DIR"
        # Рекурсивно обрабатываем файлы с расширением .py
        find "$DIR" -type f -name "*.py" | while read -r file
        do
            echo "Форматируем файл: $file"
            poetry run autopep8 --in-place --aggressive --aggressive "$file"
        done
    else
        echo "Предупреждение: Директория $DIR не найдена, пропускаем."
    fi
done

echo "Форматирование завершено!"