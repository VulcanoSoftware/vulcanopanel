#!/bin/bash

cd ..
ls
cd webssh
npm start  # start de webssh-server
ip addr show  # gebruik ip in plaats van ifconfig
echo "The webssh server is running on http://localhost:8002"
echo "don't press any key or close this window, otherwhise the program will stop"
read -p "Press any key to continue..."
