#!/bin/bash

cd ..
ls
cd webssh
npm install --production
npm start  # start de webssh-server
ip addr show  # gebruik ip in plaats van ifconfig
echo "The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1"
echo "don't press any key or close this window, otherwise the program will stop"
read -p "Press any key to continue..."
