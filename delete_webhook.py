import aiohttp
import asyncio

async def delete_webhook():
    """Принудительно удаляет webhook"""
    token = "8436678502:AAGBsDZipHNsNzrNt0NlKkFODqlmiy42esM"
    url = f"https://api.telegram.org/bot{token}/deleteWebhook"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.json()
                print(f"Результат удаления webhook: {result}")
                
                if result.get('ok'):
                    print("✅ Webhook успешно удален!")
                else:
                    print("❌ Ошибка при удалении webhook")
                    
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == '__main__':
    asyncio.run(delete_webhook())

