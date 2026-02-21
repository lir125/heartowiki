@echo off
echo Building EXE...
echo.

if not exist "venv" (
    echo Creating venv with Python 3.12...
    py -3.12 -m venv venv 2>nul
    if errorlevel 1 (
        echo ERROR: Python 3.12 not found. Install from https://www.python.org/downloads/
        echo Then delete venv folder and run this again.
        exit /b 1
    )
)

call venv\Scripts\activate.bat

echo Installing packages...
pip install -r requirements.txt -q
if errorlevel 1 (
    echo Install failed. Use Python 3.12 and delete venv then retry.
    exit /b 1
)

echo.
echo Running PyInstaller (onedir)...
pyinstaller --noconfirm --onedir --windowed --name Heartowiki --icon icon.png --add-data "index.html;." main.py

if exist "dist\Heartowiki\Heartowiki.exe" (
    echo.
    echo Done: dist\Heartowiki\Heartowiki.exe
) else (
    echo Build failed.
    exit /b 1
)
