@echo off
setlocal

rem Check if OpenSSH is installed
sc query sshd >nul 2>&1
if %errorlevel% NEQ 0 (
    echo OpenSSH is not installed. Installing...
    powershell -Command "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
    if %errorlevel% NEQ 0 (
        echo Error installing OpenSSH. Please check your system settings.
        exit /b
    )
    echo OpenSSH has been successfully installed.
) else (
    echo OpenSSH is already installed.
)

rem Start the SSH server
echo Starting the SSH server...
net start sshd

rem Check if the firewall rule for port 22 exists and create it if it does not
netsh advfirewall firewall show rule name="OpenSSH Port 22" >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Opening port 22 in the firewall...
    netsh advfirewall firewall add rule name="OpenSSH Port 22" dir=in action=allow protocol=TCP localport=22
    echo Port 22 has been opened.
) else (
    echo Port 22 is already open in the firewall.
)

echo SSH/SFTP server has started.
pause
