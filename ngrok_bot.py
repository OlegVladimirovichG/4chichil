import asyncio
import logging
from datetime import datetime, time
import pytz
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, StateFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import web
import aiohttp
import random
import os
import json

from config import BOT_TOKEN, MORNING_TIME
from monkey_photos import MONKEY_PHOTOS, LOCAL_PHOTOS

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Состояния для FSM
class BotStates(StatesGroup):
    waiting_for_first_answer = State()
    waiting_for_second_answer = State()

# Глобальная переменная для ID чата
CHAT_ID = None

# Создание клавиатур
def get_yes_no_keyboard():
    """Создает клавиатуру с кнопками Да/Нет"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data="yes"),
            InlineKeyboardButton(text="Нет", callback_data="no")
        ]
    ])
    return keyboard

def get_confirm_keyboard():
    """Создает клавиатуру с кнопкой подтверждения"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да, уверен!", callback_data="confirm"),
            InlineKeyboardButton(text="Нет, передумал", callback_data="no_confirm")
        ]
    ])
    return keyboard

# Функция для получения случайного фото обезьяны
def get_random_monkey_photo():
    """Возвращает случайное фото обезьяны"""
    return random.choice(MONKEY_PHOTOS)

async def send_monkey_photo(chat_id: int, caption: str = "🖕 Обезьяна показывает фак!"):
    """Отправляет фото обезьяны в чат"""
    try:
        photo_url = get_random_monkey_photo()
        logger.info(f"Пытаюсь отправить фото: {photo_url}")
        
        # Отправляем фото напрямую по URL
        await bot.send_photo(chat_id, photo_url, caption=caption)
        logger.info("Фото успешно отправлено")
        
    except Exception as e:
        logger.error(f"Ошибка при отправке фото: {e}")
        # Если не удалось отправить фото, отправляем заглушку
        await bot.send_message(chat_id, f"🖕 {caption}\n\nФото временно недоступно, но обезьяна все равно показывает фак!")

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    """Обработчик команды /start"""
    global CHAT_ID
    
    # Сохраняем ID чата для утренних отправок
    CHAT_ID = message.chat.id
    
    # Первый вопрос с кнопками
    await message.answer("Денис, ты хочешь посмеяться? 😏", reply_markup=get_yes_no_keyboard())
    
    # Устанавливаем состояние ожидания ответа
    await state.set_state(BotStates.waiting_for_first_answer)

@dp.callback_query(StateFilter(BotStates.waiting_for_first_answer))
async def handle_first_answer_callback(callback: types.CallbackQuery, state: FSMContext):
    """Обработчик первого ответа через кнопки"""
    await callback.answer()
    
    if callback.data == "yes":
        # Если ответ "да", задаем второй вопрос
        await callback.message.answer("Ты уверен? 🤔", reply_markup=get_confirm_keyboard())
        await state.set_state(BotStates.waiting_for_second_answer)
    else:
        # Если ответ "нет", сразу отправляем фото
        await callback.message.answer("Ну ладно, тогда вот тебе фото обезьяны! 🖕")
        await send_monkey_photo(callback.message.chat.id)
        await state.clear()

@dp.callback_query(StateFilter(BotStates.waiting_for_second_answer))
async def handle_second_answer_callback(callback: types.CallbackQuery, state: FSMContext):
    """Обработчик второго ответа через кнопки"""
    await callback.answer()
    
    # Любой ответ - отправляем фото
    await callback.message.answer("Отлично! Тогда вот тебе фото обезьяны! 🖕")
    await send_monkey_photo(callback.message.chat.id)
    await state.clear()

# Обработчики текстовых сообщений (для совместимости)
@dp.message(StateFilter(BotStates.waiting_for_first_answer))
async def handle_first_answer_text(message: types.Message, state: FSMContext):
    """Обработчик первого ответа текстом"""
    text = message.text.lower().strip()
    
    if text in ['да', 'yes', 'y', 'д', 'ага', 'конечно', 'хочу']:
        # Если ответ "да", задаем второй вопрос
        await message.answer("Ты уверен? 🤔", reply_markup=get_confirm_keyboard())
        await state.set_state(BotStates.waiting_for_second_answer)
    else:
        # Если ответ "нет" или любой другой, сразу отправляем фото
        await message.answer("Ну ладно, тогда вот тебе фото обезьяны! 🖕")
        await send_monkey_photo(message.chat.id)
        await state.clear()

@dp.message(StateFilter(BotStates.waiting_for_second_answer))
async def handle_second_answer_text(message: types.Message, state: FSMContext):
    """Обработчик второго ответа текстом"""
    text = message.text.lower().strip()
    
    # Любой ответ - отправляем фото
    await message.answer("Отлично! Тогда вот тебе фото обезьяны! 🖕")
    await send_monkey_photo(message.chat.id)
    await state.clear()

@dp.message(Command("monkey"))
async def cmd_monkey(message: types.Message):
    """Команда для получения фото обезьяны в любое время"""
    await send_monkey_photo(message.chat.id, "🖕 Вот тебе обезьяна с факом!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Команда помощи"""
    help_text = """
🖕 Бот обезьян с факом!

Команды:
/start - Начать игру с вопросами
/monkey - Получить фото обезьяны прямо сейчас
/help - Показать эту справку

Бот автоматически отправляет фото обезьян каждое утро в 8:00 по МСК! 🕗
    """
    await message.answer(help_text)

async def send_morning_photo():
    """Отправляет утреннее фото обезьяны"""
    global CHAT_ID
    if CHAT_ID:
        try:
            await send_monkey_photo(CHAT_ID, "🖕 Доброе утро! Обезьяна показывает фак! 🌅")
            logger.info(f"Утреннее фото отправлено в чат {CHAT_ID}")
        except Exception as e:
            logger.error(f"Ошибка при отправке утреннего фото: {e}")

# Webhook обработчики
async def webhook_handler(request):
    """Обработчик webhook от Telegram"""
    try:
        update = types.Update(**await request.json())
        await dp.feed_update(bot, update)
        return web.Response(status=200)
    except Exception as e:
        logger.error(f"Ошибка в webhook: {e}")
        return web.Response(status=500)

async def on_startup(app):
    """Действия при запуске приложения"""
    logger.info("Веб-приложение запущено!")
    
    # Запускаем планировщик утренних фото
    asyncio.create_task(schedule_morning_photo())

async def on_shutdown(app):
    """Действия при остановке приложения"""
    logger.info("Веб-приложение останавливается...")
    await bot.session.close()

async def schedule_morning_photo():
    """Планировщик для отправки фото каждое утро в 8:00 МСК"""
    msk_tz = pytz.timezone('Europe/Moscow')
    
    while True:
        try:
            now = datetime.now(msk_tz)
            target_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
            
            # Если уже прошло 8:00, планируем на завтра
            if now.time() >= time(8, 0):
                target_time = target_time.replace(day=target_time.day + 1)
            
            # Ждем до целевого времени
            seconds_until_target = (target_time - now).total_seconds()
            await asyncio.sleep(seconds_until_target)
            
            # Отправляем фото
            await send_morning_photo()
            
            # Ждем до следующего дня
            await asyncio.sleep(86400)  # 24 часа
            
        except Exception as e:
            logger.error(f"Ошибка в планировщике: {e}")
            await asyncio.sleep(60)  # Ждем минуту перед повторной попыткой

# Создание веб-приложения
app = web.Application()
app.router.add_post('/webhook', webhook_handler)
app.router.add_get('/', lambda r: web.Response(text="🖕 Бот обезьян с факом работает на ngrok!"))

app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)

