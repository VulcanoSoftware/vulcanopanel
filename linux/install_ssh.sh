#!/bin/bash

cd ..
ls
cd webssh
npm install --production
npm start
ifconfig
echo "The webssh server is running on http://localhost:8002/ssh/host/127.0.0.1"
echo "don't press any key or close this window, otherwhise the program will stop"
read -p "Press any key to continue..."
