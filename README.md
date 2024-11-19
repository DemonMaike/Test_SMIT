# About
This is a test exercise for Python Middle Developer position at SMIT.Studio company.

## Main Packages:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose
- pytest
- Pydantic / Pydantic-settings
- Poetry

## Map
You can see:
- [API Table](docs/api_table.md)
- [Project Structure](docs/project_structure.md)

For class diagram and use case, please use draw.io

## Quick Start
1. Update your .env file by renaming .env-example from the root directory:
```shell
mv src/.env-example src/.env
```

2. Verify environment parsing by running from root directory:
```shell
python settings.py
```

You should see output similar to:
```shell
{'db': {'host': 'db', 'port': 5432, 'user': 'postgres', 'passwd': 'postgres', 'name': 'smit'}}
```

If the output is different, check your .env file or the DatabaseSetting class in settings.py.

3. Start the application using Docker Compose from the project root:
```shell
docker-compose -f ./docker/docker-compose.yml up --build -d
```
(Remove "-d" flag to see real-time logs)

4. Access Swagger UI at http://127.0.0.1:8000/docs

5. Test the /rates/ route using the provided catgo-rates.json file in src/tests/tests_files.

6. Upload the file to test data loading into the database.

7. Use the /calculate/ endpoint to calculate insurance cost by modifying declared_value, cargo_type, and date as needed.

# О проекте
Это тестовое задание на позицию Python Middle разработчика в компании SMIT.Studio.

## Основные пакеты:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose
- pytest
- Pydantic / Pydantic-settings
- Poetry

## Карта проекта
Вы можете посмотреть:
- [Таблицу API](docs/api_table.md)
- [Структуру проекта](docs/project_structure.md)

Для просмотра диаграммы классов и use case используйте draw.io

## Быстрый старт
1. Обновите файл .env, переименовав .env-example из корневой директории:
```shell
mv src/.env-example src/.env
```

2. Проверьте парсинг окружения, выполнив из корневой директории:
```shell
python settings.py
```

Вы должны увидеть вывод, похожий на:
```shell
{'db': {'host': 'db', 'port': 5432, 'user': 'postgres', 'passwd': 'postgres', 'name': 'smit'}}
```

Если вывод отличается, проверьте ваш файл .env или класс DatabaseSetting в settings.py.

3. Запустите приложение с помощью Docker Compose из корня проекта:
```shell
docker-compose -f ./docker/docker-compose.yml up --build -d
```
(Удалите флаг "-d" для просмотра логов в реальном времени)

4. Откройте Swagger UI по адресу http://127.0.0.1:8000/docs

5. Протестируйте маршрут /rates/, используя предоставленный файл catgo-rates.json в src/tests/tests_files.

6. Загрузите файл для тестирования загрузки данных в базу данных.

7. Используйте конечную точку /calculate/ для расчета стоимости страховки, изменяя declared_value, cargo_type и дату по необходимости.
