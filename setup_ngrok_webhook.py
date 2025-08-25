#!/usr/bin/env python3
"""
Скрипт для автоматической настройки webhook с ngrok
"""

import aiohttp
import asyncio
import sys

async def setup_webhook(ngrok_url: str):
    """Настраивает webhook для бота"""
    token = "8436678502:AAGBsDZipHNsNzrNt0NlKkFODqlmiy42esM"
    webhook_url = f"{ngrok_url}/webhook"
    
    # Сначала удаляем старый webhook
    delete_url = f"https://api.telegram.org/bot{token}/deleteWebhook"
    async with aiohttp.ClientSession() as session:
        async with session.get(delete_url) as response:
            result = await response.json()
            print(f"Удаление старого webhook: {result}")
    
    # Устанавливаем новый webhook
    set_url = f"https://api.telegram.org/bot{token}/setWebhook?url={webhook_url}"
    async with aiohttp.ClientSession() as session:
        async with session.get(set_url) as response:
            result = await response.json()
            print(f"Установка нового webhook: {result}")
            
            if result.get('ok'):
                print(f"✅ Webhook успешно установлен: {webhook_url}")
                print(f"🌐 Проверь сайт: {ngrok_url}")
                print(f"🤖 Теперь протестируй бота в Telegram!")
            else:
                print(f"❌ Ошибка при установке webhook: {result}")

def main():
    if len(sys.argv) != 2:
        print("Использование: python setup_ngrok_webhook.py <ngrok_url>")
        print("Пример: python setup_ngrok_webhook.py https://abc123.ngrok.io")
        return
    
    ngrok_url = sys.argv[1]
    if not ngrok_url.startswith('https://'):
        ngrok_url = f"https://{ngrok_url}"
    
    print(f"🚀 Настройка webhook для ngrok URL: {ngrok_url}")
    asyncio.run(setup_webhook(ngrok_url))

if __name__ == '__main__':
    main()

