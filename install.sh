#!/bin/bash

# Change directory to linux
cd linux

# Run installation scripts
./install_ssh.sh
./install_sftp.sh

# Open the specified ports in the firewall
sudo firewall-cmd --add-port=8000/tcp --permanent
sudo firewall-cmd --add-port=8001/tcp --permanent
sudo firewall-cmd --add-port=8002/tcp --permanent
sudo firewall-cmd --reload

# Display network configuration
ifconfig

# Display server information
echo "The webserver is running on http://localhost:8000/"
echo "The sftp server is running on http://localhost:8001/"
echo "The webssh server is running on http://localhost:8002/ssh/host/127.0.0.1"
echo "Don't press any key or close this window, otherwise the program will stop."

# Wait for user input
read -p "Press any key to continue..."
