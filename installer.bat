@echo off
echo Starting installation of XAMPP, Node.js, Python, and Git...

:: Set the download URLs
set XAMPP_URL=https://deac-fra.dl.sourceforge.net/project/xampp/XAMPP%20Windows/8.2.12/xampp-windows-x64-8.2.12-0-VS16-installer.exe?viasf=1
set NODEJS_URL=https://nodejs.org/dist/v18.0.0/node-v18.0.0-x64.msi
set PYTHON_URL=https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe
set GIT_URL=https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.1/Git-2.41.0-64-bit.exe

:: Set the download locations
set DOWNLOAD_DIR=%TEMP%\installers
mkdir %DOWNLOAD_DIR%

:: Download the installers
echo Downloading XAMPP...
powershell -Command "Invoke-WebRequest -Uri %XAMPP_URL% -OutFile %DOWNLOAD_DIR%\xampp.exe"

echo Downloading Node.js...
powershell -Command "Invoke-WebRequest -Uri %NODEJS_URL% -OutFile %DOWNLOAD_DIR%\nodejs.msi"

echo Downloading Python...
powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %DOWNLOAD_DIR%\python.exe"

echo Downloading Git...
powershell -Command "Invoke-WebRequest -Uri %GIT_URL% -OutFile %DOWNLOAD_DIR%\git.exe"

:: Install XAMPP
echo Installing XAMPP...
start /wait %DOWNLOAD_DIR%\xampp.exe /SILENT

:: Install Node.js
echo Installing Node.js...
msiexec /i %DOWNLOAD_DIR%\nodejs.msi /quiet /norestart

:: Install Python
echo Installing Python...
start /wait %DOWNLOAD_DIR%\python.exe /quiet InstallAllUsers=1 PrependPath=1

:: Install Git
echo Installing Git...
start /wait %DOWNLOAD_DIR%\git.exe /VERYSILENT /NORESTART

echo Installation completed.

:: Cleanup
echo Cleaning up...
rd /s /q %DOWNLOAD_DIR%

pause
