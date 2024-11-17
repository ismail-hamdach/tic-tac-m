@echo off
echo Starting the process for the Python app...

:: Set repository URL
set PYTHON_REPO=https://github.com/ismail-hamdach/tic-tac-m.git

:: Set directory
set PYTHON_DIR=%~dp0python-app

:: Clone the Python repository
echo Cloning the Python repository...
git clone %PYTHON_REPO% %PYTHON_DIR%

:: Install dependencies for Python app
echo Installing dependencies for Python app...
cd %PYTHON_DIR%
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

:: Run the Python app
echo Starting the Python app...
start "" python app.py

echo Python process completed.

pause
