@echo off
REM Installs fnm (Fast Node Manager) via PowerShell
powershell -Command "Invoke-WebRequest -Uri https://fnm.vercel.app/install -UseBasicParsing | Invoke-Expression"

REM Activate fnm by adding it to the PATH (this may vary depending on where fnm is installed)
REM You might need to restart your terminal after installation to apply changes

REM Download and install Node.js version 20 using fnm
fnm use --install-if-missing 20

REM Verifies the right Node.js version is in the environment
node -v

REM Verifies the right npm version is in the environment
npm -v

pause
