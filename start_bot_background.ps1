# PowerShell script for starting bot in background
Write-Host "Starting monkey bot in background..." -ForegroundColor Green
Write-Host ""

# Change to script directory
Set-Location $PSScriptRoot

# Start web application in background
Write-Host "Starting web application..." -ForegroundColor Yellow
Start-Process python -ArgumentList "ngrok_bot.py" -WindowStyle Hidden

# Wait for web app to start
Write-Host "Waiting 5 seconds for web app to start..." -ForegroundColor Cyan
Start-Sleep -Seconds 5

# Start ngrok in background
Write-Host "Starting ngrok tunnel..." -ForegroundColor Yellow
Start-Process ngrok -ArgumentList "http 8000" -WindowStyle Hidden

# Wait for ngrok to start
Write-Host "Waiting 10 seconds for ngrok to start..." -ForegroundColor Cyan
Start-Sleep -Seconds 10

# Get ngrok URL
Write-Host "Getting ngrok URL..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "http://localhost:4040/api/tunnels" -Method Get
    $ngrokUrl = $response.tunnels[0].public_url
    
    Write-Host ""
    Write-Host "Ngrok URL: $ngrokUrl" -ForegroundColor Green
    Write-Host ""
    
    # Setup webhook
    Write-Host "Setting up webhook..." -ForegroundColor Yellow
    python setup_ngrok_webhook.py $ngrokUrl
    
    Write-Host ""
    Write-Host "Bot started in background!" -ForegroundColor Green
    Write-Host "Check website: $ngrokUrl" -ForegroundColor Cyan
    Write-Host "Test bot in Telegram!" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "To stop bot use: stop_bot.ps1" -ForegroundColor Yellow
    
} catch {
    Write-Host "Error getting ngrok URL: $_" -ForegroundColor Red
    Write-Host "Check if ngrok started" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

