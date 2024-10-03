@echo off

REM Ga een directory omhoog
cd ..

REM Lijst bestanden en mappen op
dir

REM Ga naar de webssh map
cd webssh

REM Start de npm server
npm start

REM Toon netwerkconfiguratie
ipconfig

REM Toon serverinformatie
echo The webssh server is running on http://localhost:8002/ssh/host/127.0.0.1

echo Don't press any key or close this window, otherwise the program will stop.

REM Wacht op gebruikersinvoer
pause
