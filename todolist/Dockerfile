# Wybierz obraz bazowy z Pythonem
FROM python:3.10-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /todolist

# Skopiuj zawartość bieżącego katalogu do katalogu /todolist w kontenerze
COPY . /todolist

RUN pip install --no-cache-dir -r /todolist/requirements.txt

RUN apt-get update
# Ustaw domyślną komendę do uruchomienia aplikacji Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001", "--no-debugger"]
