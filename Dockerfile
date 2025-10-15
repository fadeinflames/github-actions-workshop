FROM python:3.11-slim

WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app/ ./app/

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "-m", "app.api"]
