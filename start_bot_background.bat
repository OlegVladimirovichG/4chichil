@echo off
echo 🚀 Запуск бота обезьян с факом в фоне...
echo.

cd /d "%~dp0"

echo 📱 Запуск веб-приложения бота...
start /min pythonw ngrok_bot.py

echo ⏳ Ждем 5 секунд для запуска веб-приложения...
timeout /t 5 /nobreak >nul

echo 🌐 Запуск ngrok туннеля...
start /min ngrok.exe http 8000

echo ⏳ Ждем 10 секунд для запуска ngrok...
timeout /t 10 /nobreak >nul

echo 🔗 Получение ngrok URL...
for /f "tokens=*" %%i in ('curl -s http://localhost:4040/api/tunnels ^| python -c "import sys, json; data=json.load(sys.stdin); print(data['tunnels'][0]['public_url'] if data['tunnels'] else 'ERROR')"') do set NGROK_URL=%%i

echo.
echo 🎯 Ngrok URL: %NGROK_URL%
echo.

echo 🔧 Настройка webhook...
python setup_ngrok_webhook.py %NGROK_URL%

echo.
echo ✅ Бот запущен в фоне!
echo 🌐 Проверь сайт: %NGROK_URL%
echo 🤖 Протестируй бота в Telegram!
echo.
echo 💡 Для остановки бота используй: stop_bot.bat
pause

