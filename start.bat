@echo off

REM Verander directory naar linux
cd windows

REM Start de SSH en SFTP scripts op de achtergrond
start /b start_ssh.bat
start /b start_sftp.bat

REM Toon netwerkconfiguratie
ipconfig

REM Toon server URL's
echo The webserver is running on http://localhost:8000/
echo The sftp server is running on http://localhost:8001/
echo The webssh server is running on http://localhost:8002/ssh/host/127.0.0.1

echo Don't press any key or close this window, otherwise the program will stop.

REM Wacht op gebruikersinvoer
pause
