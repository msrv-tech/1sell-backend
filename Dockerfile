FROM python:3.10-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода
COPY alembic.ini .

# Команда для запуска Celery
CMD ["celery", "-A", "app.tasks.sync_1c", "worker", "--loglevel=info"]

# Запуск миграций и приложения
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000