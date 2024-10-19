# Используйте официальный образ Python как базовый
FROM python:3.10

# Установите рабочую директорию
WORKDIR /app

# Копируйте файлы зависимостей
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте проект в контейнер
COPY . .

# Запустите сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
