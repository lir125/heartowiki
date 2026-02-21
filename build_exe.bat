@echo off
chcp 437 >nul
echo Building EXE...
echo.

if exist venv\Scripts\activate.bat goto activate
echo Creating venv...
py -3.12 -m venv venv
if errorlevel 1 python -m venv venv
if not exist venv\Scripts\activate.bat (
    echo ERROR: Python not found.
    pause
    exit /b 1
)

:activate
call venv\Scripts\activate.bat

echo Installing packages...
pip install -r requirements.txt -q
if errorlevel 1 (
    echo Install failed.
    pause
    exit /b 1
)

echo.
echo Creating icon.ico from icon.png...
python png_to_ico.py
if exist icon.ico (
    echo Using icon.ico
    pyinstaller --noconfirm --onefile --windowed --name Heartowiki --icon icon.ico --add-data "index.html;." --distpath . --workpath build --specpath . main.py
) else (
    echo Warning: icon.ico not created, using icon.png
    pyinstaller --noconfirm --onefile --windowed --name Heartowiki --icon icon.png --add-data "index.html;." --distpath . --workpath build --specpath . main.py
)

if exist Heartowiki.exe (
    echo.
    echo Done. See Heartowiki.exe
) else (
    echo Build failed.
    exit /b 1
)
pause
