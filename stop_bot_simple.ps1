# Simple script to stop the monkey bot
Write-Host "Stopping monkey bot..." -ForegroundColor Red

# Stop Python processes running ngrok_bot.py
Get-Process python -ErrorAction SilentlyContinue | Where-Object {
    $_.ProcessName -eq "python" -and 
    (Get-WmiObject Win32_Process -Filter "ProcessId = $($_.Id)").CommandLine -like "*ngrok_bot.py*"
} | Stop-Process -Force

# Stop ngrok processes
Get-Process ngrok -ErrorAction SilentlyContinue | Stop-Process -Force

Write-Host "Bot stopped!" -ForegroundColor Green
