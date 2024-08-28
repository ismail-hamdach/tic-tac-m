@echo off
echo Starting the process for the Next.js app...

:: Set repository URL
set NEXTJS_REPO=https://github.com/ismail-hamdach/tic-tac-m-web-app.git

:: Set directory
set NEXTJS_DIR=%~dp0nextjs-app

:: Clone the Next.js repository
echo Cloning the Next.js repository...
git clone %NEXTJS_REPO% %NEXTJS_DIR%

:: Install dependencies for Next.js app
echo Installing dependencies for Next.js app...
cd %NEXTJS_DIR%
npm install

:: Build the Next.js app
echo Building the Next.js app...
npm run build

:: Run the Next.js app
echo Starting the Next.js app...
start "" npm run start

echo Next.js process completed.

pause
