@echo off

REM Verander directory naar linux
cd windows

REM Voer de installatie scripts uit
call install_ssh.bat
call install_sftp.bat

REM Open de opgegeven poorten in de firewall
netsh advfirewall firewall add rule name="Open Port 4340" protocol=TCP dir=in localport=4340 action=allow
netsh advfirewall firewall add rule name="Open Port 2222" protocol=TCP dir=in localport=2222 action=allow

REM Toon netwerkconfiguratie
ipconfig

REM Toon serverinformatie
echo The sftp server is running on http://localhost:4340/
echo The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1
echo Don't press any key or close this window, otherwise the program will stop.

REM Wacht op gebruikersinvoer
pause
