import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, '/home/yourusername/4chichil')

# Импортируем веб-приложение
from webhook_bot import app

# Создаем WSGI приложение
application = app
