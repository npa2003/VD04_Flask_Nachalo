from flask import Flask, render_template
from datetime import datetime
from pathlib import Path
import os

# Определяем абсолютный путь к папке с шаблонами
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / 'templates'

# Проверяем существование папки
if not TEMPLATES_DIR.exists():
    raise FileNotFoundError(
        f"Папка с шаблонами не найдена по пути: {TEMPLATES_DIR}\n"
        "Проверьте:\n"
        "1. Что папка называется 'templates'\n"
        "2. Что она находится в одной директории с app.py"
    )

app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

@app.route('/')
def show_time():
    now = datetime.now()
    return render_template(
        'index.html',
        time=now.strftime("%H:%M:%S"),
        date=now.strftime("%d.%m.%Y")
    )

if __name__ == '__main__':
    print(f"Запуск из: {BASE_DIR}")
    print(f"Шаблоны в: {TEMPLATES_DIR}")
    print(f"Содержимое templates: {os.listdir(TEMPLATES_DIR)}")
    app.run(debug=True)