FROM python:3.11

# Рабочая директория
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY /requirements.txt /

# Запускаем команду для установки зависимостей. --no-cache-dir - не кэшурется список зависимостей, чтобы устанавливались актуальные версии.
RUN pip install -r /requirements.txt --no-cache-dir

# Копируем всё в рабочую директорию
COPY . .
