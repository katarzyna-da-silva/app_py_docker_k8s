from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Konfiguracja CORS

# Lista zadań - przykładowa implementacja, w praktyce dane przechowywane byłyby np. w bazie danych
tasks = {'todo': [], 'in-progress': [], 'done': []}

# Pobranie imienia z zmiennej środowiskowej lub ustawienie domyślnego imienia
user_name = os.getenv('VOTREPRENOM', 'Anonymous')

@app.route('/')
def index():
    return render_template('index.html', user_name=user_name, tasks=tasks)

@app.route('/add', methods=['GET'])
def add_task_form():
    return render_template('add_task.html')

@app.route('/add', methods=['POST'])
def add_task_logic():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_content = request.form['task_content']
        task_category = request.form['task_category']
        
        # Dodawanie zadania do odpowiedniej kategorii
        tasks[task_category].append({'name': task_name, 'content': task_content})
        print(tasks)
        return redirect(url_for('index'))
    print(tasks)

@app.route('/mark_task_in_progress/<task_name>', methods=['POST'])
def mark_task_in_progress(task_name):
    # Znajdź zadanie o podanej nazwie w liście zadań "todo" i przenieś je do listy "in-progress"
    for idx, task in enumerate(tasks['todo']):
        if task['name'] == task_name:
            tasks['in-progress'].append(tasks['todo'].pop(idx))
            break
    return redirect(url_for('index'))

@app.route('/mark_task_done/<task_name>', methods=['POST'])
def mark_task_done(task_name):
    # Znajdź zadanie o podanej nazwie w liście zadań "in-progress" i przenieś je do listy "done"
    for idx, task in enumerate(tasks['in-progress']):
        if task['name'] == task_name:
            tasks['done'].append(tasks['in-progress'].pop(idx))
            break
    return redirect(url_for('index'))

@app.route('/remove_task/<task_name>', methods=['POST'])
def remove_task(task_name):
    # Usuń zadanie o podanej nazwie z dowolnej listy zadań, w której się znajduje
    for column in tasks:
        for idx, task in enumerate(tasks[column]):
            if task['name'] == task_name:
                tasks[column].pop(idx)
                break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)