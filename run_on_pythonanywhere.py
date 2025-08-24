#!/usr/bin/env python3
"""
Скрипт для запуска бота на PythonAnywhere через консоль
Запускайте в разделе Consoles -> Bash
"""

import subprocess
import sys
import os

def main():
    print("🚀 Запуск бота обезьян с факом на PythonAnywhere...")
    
    # Проверяем наличие необходимых файлов
    required_files = ['simple_bot.py', 'config.py', 'monkey_photos.py']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Отсутствуют файлы: {', '.join(missing_files)}")
        print("Убедитесь, что все файлы загружены в PythonAnywhere")
        return
    
    # Устанавливаем зависимости
    print("📦 Установка зависимостей...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--user', 'aiogram', 'python-dotenv', 'pytz', 'aiohttp'], check=True)
        print("✅ Зависимости установлены")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка установки зависимостей: {e}")
        return
    
    # Запускаем бота
    print("🤖 Запуск бота...")
    try:
        subprocess.run([sys.executable, 'simple_bot.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка запуска бота: {e}")
    except KeyboardInterrupt:
        print("\n⏹️ Бот остановлен пользователем")

if __name__ == '__main__':
    main()
