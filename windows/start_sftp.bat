@echo off

REM Ga een directory omhoog
cd ..

REM Ga naar de sftp_web_client map
cd sftp_web_client

REM Lijst bestanden en mappen op
dir

REM Start de Node.js applicatie
node src\main.js start

REM Toon netwerkconfiguratie
ipconfig

REM Toon serverinformatie
echo The sftp server is running on http://localhost:8001/

echo Don't press any key or close this window, otherwise the program will stop.

REM Wacht op gebruikersinvoer
pause
