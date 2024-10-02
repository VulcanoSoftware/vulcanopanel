@echo off

REM Ga een directory omhoog
cd ..

REM Lijst bestanden en mappen op
dir

REM Ga naar de sftp_web_client map
cd sftp_web_client

REM Installeer npm packages in productie modus
npm install --production

REM Start de wfc service (vervang door een geschikt Windows commando indien nodig)
wfc start

REM Toon netwerkconfiguratie
ipconfig

REM Toon serverinformatie
echo The sftp server is running on http://localhost:4340/

echo Don't press any key or close this window, otherwise the program will stop.

REM Wacht op gebruikersinvoer
pause
