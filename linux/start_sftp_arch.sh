#!/bin/bash

cd ..
cd sftp_web_client
ls
node src/main.js start  # start de SFTP-server
ip addr show  # gebruik ip in plaats van ifconfig
echo "The sftp server is running on http://localhost:8001/"
echo "don't press any key or close this window, otherwise the program will stop"
read -p "Press any key to continue..."
