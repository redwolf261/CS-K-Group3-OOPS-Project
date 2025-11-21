# Launch AES GUI - Modern Version
# This script launches the modern CustomTkinter GUI

Write-Host "Starting AES Encryption Tool GUI (Modern)..." -ForegroundColor Green
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

# Check if customtkinter is installed
Write-Host "Checking for customtkinter..." -ForegroundColor Cyan
python -c "import customtkinter" 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "CustomTkinter not found. Installing..." -ForegroundColor Yellow
    pip install customtkinter
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Failed to install customtkinter" -ForegroundColor Red
        Write-Host "You can use the basic GUI instead: launch_gui.ps1" -ForegroundColor Yellow
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "CustomTkinter installed successfully!" -ForegroundColor Green
} else {
    Write-Host "CustomTkinter is already installed." -ForegroundColor Green
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
Write-Host "Launching Modern GUI..." -ForegroundColor Green
python aes_gui_modern.py
