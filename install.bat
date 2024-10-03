@echo off

REM Verander directory naar linux
cd windows

REM Voer de installatie scripts uit
call install_ssh.bat
call install_sftp.bat

REM Open de opgegeven poorten in de firewall
netsh advfirewall firewall add rule name="Open Port 8000" protocol=TCP dir=in localport=8000 action=allow
netsh advfirewall firewall add rule name="Open Port 8001" protocol=TCP dir=in localport=8001 action=allow
netsh advfirewall firewall add rule name="Open Port 8002" protocol=TCP dir=in localport=8002 action=allow

REM Toon netwerkconfiguratie
ipconfig

REM Toon serverinformatie
echo The webserver is running on http://localhost:8000/
echo The sftp server is running on http://localhost:8001/
echo The webssh server is running on http://localhost:8002/ssh/host/127.0.0.1
echo Don't press any key or close this window, otherwise the program will stop.

REM Wacht op gebruikersinvoer
pause
