#!/bin/bash

cd ..
cd sftp_web_client
ls
node src/main.js start
ifconfig
echo "The sftp server is running on http://localhost:4340/"
echo "don't press any key or close this window, otherwhise the program will stop"
read -p "Press any key to continue..."
