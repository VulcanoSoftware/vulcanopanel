#!/bin/bash

cd linux
# Start the SSH and SFTP scripts in the background
./start_ssh.sh &
./start_sftp.sh &

# Display network configuration
ip a

# Display server URLs
echo "The webserver is running on http://localhost:8000/"
echo "The sftp server is running on http://localhost:8001/"
echo "The webssh server is running on http://localhost:8002/ssh/host/127.0.0.1"

echo "don't press any key or close this window, otherwhise the program will stop"
# Wait for user input
read -p "Press any key to continue..."
