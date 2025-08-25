# PowerShell скрипт для остановки бота
Write-Host "🛑 Остановка бота обезьян с факом..." -ForegroundColor Red
Write-Host ""

# Останавливаем веб-приложение
Write-Host "📱 Остановка веб-приложения..." -ForegroundColor Yellow
Get-Process python -ErrorAction SilentlyContinue | Where-Object {$_.ProcessName -eq "python"} | Stop-Process -Force -ErrorAction SilentlyContinue
Get-Process pythonw -ErrorAction SilentlyContinue | Where-Object {$_.ProcessName -eq "pythonw"} | Stop-Process -Force -ErrorAction SilentlyContinue

# Останавливаем ngrok
Write-Host "🌐 Остановка ngrok..." -ForegroundColor Yellow
Get-Process ngrok -ErrorAction SilentlyContinue | Where-Object {$_.ProcessName -eq "ngrok"} | Stop-Process -Force -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "✅ Бот остановлен!" -ForegroundColor Green
Write-Host "💡 Для запуска используй: start_bot_background.ps1" -ForegroundColor Cyan

Write-Host ""
Write-Host "Нажмите любую клавишу для продолжения..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

