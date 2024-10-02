#!/bin/bash

cd ..
ls
cd sftp_web_client
npm install --production
sudo service wfc start
ifconfig
echo "The sftp server is running on http://localhost:4340/"
echo "don't press any key or close this window, otherwhise the program will stop"
read -p "Press any key to continue..."
