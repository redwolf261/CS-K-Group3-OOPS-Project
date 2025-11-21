# Launch AES GUI - Basic Version
# This script launches the basic tkinter GUI

Write-Host "Starting AES Encryption Tool GUI..." -ForegroundColor Green
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Cyan
} catch {
    Write-Host "ERROR: Python not found. Please install Python 3.7 or higher." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if executable exists
$exePath = Join-Path $PSScriptRoot "ProjectAES\aes_tool.exe"
if (-not (Test-Path $exePath)) {
    Write-Host "WARNING: C++ executable not found at: $exePath" -ForegroundColor Yellow
    Write-Host "Please build the C++ backend first." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To build, run:" -ForegroundColor Cyan
    Write-Host "  cd ProjectAES" -ForegroundColor White
    Write-Host "  g++ -std=c++11 -Wall main.cpp AES.cpp FileHandler.cpp Logger.cpp -o aes_tool.exe" -ForegroundColor White
    Write-Host ""
    Read-Host "Press Enter to continue anyway (GUI will show error)"
}

# Launch GUI
Write-Host ""
Write-Host "Launching GUI..." -ForegroundColor Green
python aes_gui.py
