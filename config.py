import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
BOT_TOKEN = "8436678502:AAGBsDZipHNsNzrNt0NlKkFODqlmiy42esM"

# Время отправки утренних фото (МСК)
MORNING_TIME = "08:00"

# ID чата для отправки (будет установлен при первом запуске)
CHAT_ID = None

# Состояния для FSM
class States:
    waiting_for_first_answer = "waiting_for_first_answer"
    waiting_for_second_answer = "waiting_for_second_answer"
