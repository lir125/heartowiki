@echo off
echo Building EXE...
echo.
echo On Windows, pywebview needs pythonnet, which requires Python 3.12 (not 3.14).
echo.

if not exist "venv" (
    echo Creating venv with Python 3.12...
    py -3.12 -m venv venv 2>nul
    if errorlevel 1 (
        echo.
        echo ERROR: Python 3.12 not found.
        echo Install Python 3.12 from https://www.python.org/downloads/
        echo Run "py -3.12" in cmd to verify. Then delete the "venv" folder and run this again.
        echo.
        exit /b 1
    )
)
call venv\Scripts\activate.bat

echo Installing packages (may take a few minutes)...
pip install -r requirements.txt -q
if errorlevel 1 (
    echo.
    echo Install failed. If pythonnet failed, make sure you use Python 3.12: delete "venv" and run again.
    exit /b 1
)

echo.
echo Running PyInstaller...
pyinstaller --noconfirm --onefile --windowed --name Heartowiki --add-data "index.html;." main.py

if exist "dist\Heartowiki.exe" (
    echo.
    echo Done: dist\Heartowiki.exe
    echo You can rename it and set drive_file_id in config.json.
) else (
    echo Build failed.
    exit /b 1
)
