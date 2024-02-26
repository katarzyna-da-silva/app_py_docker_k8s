# Wybierz obraz bazowy z Pythonem
FROM python:3.10-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app_py_docker_k8s/todolist

# Skopiuj zawartość bieżącego katalogu do katalogu /app w kontenerze
COPY . /app

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
# Ustaw domyślną komendę do uruchomienia aplikacji Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001", "--no-debugger"]
