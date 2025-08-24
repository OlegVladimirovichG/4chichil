# 🚀 Деплой бота на PythonAnywhere

## 📋 Шаги для деплоя:

### 1. Создание аккаунта на PythonAnywhere
- Зайдите на [www.pythonanywhere.com](https://www.pythonanywhere.com)
- Создайте бесплатный аккаунт
- Запомните ваше имя пользователя

### 2. Загрузка файлов
- В PythonAnywhere откройте **Files** → **Upload a file**
- Загрузите все файлы проекта:
  - `webhook_bot.py`
  - `config.py`
  - `monkey_photos.py`
  - `passenger_wsgi.py`
  - `requirements.txt`

### 3. Установка зависимостей
- Откройте **Consoles** → **Bash**
- Выполните команды:
```bash
cd ~/4chichil
pip3 install --user aiogram python-dotenv pytz aiohttp
```

### 4. Настройка веб-приложения
- Откройте **Web** → **Add a new web app**
- Выберите **Manual configuration**
- Python version: **Python 3.9** (или новее)
- Source code: `/home/yourusername/4chichil`
- Working directory: `/home/yourusername/4chichil`

### 5. Настройка WSGI файла
- В разделе **Code** найдите **WSGI configuration file**
- Замените содержимое на код из `passenger_wsgi.py`
- **ВАЖНО**: Замените `yourusername` на ваше реальное имя пользователя

### 6. Настройка webhook
- В файле `webhook_bot.py` найдите строку:
```python
webhook_url = f"https://yourusername.pythonanywhere.com/webhook"
```
- Замените `yourusername` на ваше реальное имя пользователя

### 7. Перезапуск приложения
- Нажмите **Reload** в разделе **Web**

## 🔧 Проверка работы:

1. **Откройте ваш сайт**: `https://yourusername.pythonanywhere.com`
2. **Должно появиться**: "🖕 Бот обезьян с факом работает!"
3. **Протестируйте бота**: напишите `/start` в Telegram

## ⚠️ Важные моменты:

- **Бесплатный аккаунт**: имеет ограничения на время работы
- **Webhook**: работает только на платных аккаунтах
- **Логи**: смотрите в разделе **Web** → **Log files**

## 🆘 Если что-то не работает:

1. **Проверьте логи** в разделе **Web** → **Error log**
2. **Убедитесь**, что все зависимости установлены
3. **Проверьте**, что webhook URL правильный
4. **Перезапустите** приложение

## 💰 Платный аккаунт (рекомендуется):

Для стабильной работы бота лучше использовать платный аккаунт:
- Бот будет работать 24/7
- Webhook будет работать стабильно
- Больше ресурсов и возможностей

## 📱 Команды бота после деплоя:

- `/start` - Начать игру с вопросами
- `/monkey` - Получить фото обезьяны
- `/help` - Справка

Бот будет автоматически отправлять фото гориллы каждое утро в 8:00 по МСК! 🖕
