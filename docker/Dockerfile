FROM python:3.12-slim


RUN apt-get update && apt-get install -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src src
COPY settings.py .

EXPOSE 8000

# Команда для запуска FastAPI сервера
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
