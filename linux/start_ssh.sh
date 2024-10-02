#!/bin/bash

cd ..
ls
cd webssh
npm start
ifconfig
echo "The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1"
echo "don't press any key or close this window, otherwhise the program will stop"
read -p "Press any key to continue..."
