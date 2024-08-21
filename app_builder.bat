@echo off
echo Starting the process...

:: Set repository URLs
set NEXTJS_REPO=https://github.com/ismail-hamdach/tic-tac-m-web-app.git
set PYTHON_REPO=https://github.com/ismail-hamdach/tic-tac-m.git

:: Set directories
set NEXTJS_DIR=%~dp0nextjs-app
set PYTHON_DIR=%~dp0python-app

:: Clone the Next.js repository
echo Cloning the Next.js repository...
git clone %NEXTJS_REPO% %NEXTJS_DIR%

:: Clone the Python repository
echo Cloning the Python repository...
git clone %PYTHON_REPO% %PYTHON_DIR%

:: Install dependencies for Next.js app
echo Installing dependencies for Next.js app...
cd %NEXTJS_DIR%
npm install

:: Build the Next.js app
echo Building the Next.js app...
npm run build

:: Install dependencies for Python app
echo Installing dependencies for Python app...
cd %PYTHON_DIR%
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

:: Run the Next.js app
echo Starting the Next.js app...
cd %NEXTJS_DIR%
start "" npm run start

:: Run the Python app
echo Starting the Python app...
cd %PYTHON_DIR%
start "" python app.py

echo Process completed.

pause
