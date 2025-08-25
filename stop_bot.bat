@echo off
echo 🛑 Остановка бота обезьян с факом...
echo.

echo 📱 Остановка веб-приложения...
taskkill /f /im pythonw.exe 2>nul
taskkill /f /im python.exe 2>nul

echo 🌐 Остановка ngrok...
taskkill /f /f /im ngrok.exe 2>nul

echo.
echo ✅ Бот остановлен!
echo 💡 Для запуска используй: start_bot_background.bat
pause

