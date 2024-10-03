#!/bin/bash

# Change directory to linux
cd linux

# Run installation scripts
./install_ssh_arch.sh
./install_sftp_arch.sh

# Open the specified ports in the firewall
sudo ufw allow 8000/tcp
sudo ufw allow 8001/tcp
sudo ufw allow 8002/tcp
sudo ufw reload

# Display network configuration
ip addr

# Display server information
echo "The webserver is running on http://localhost:8000/"
echo "The sftp server is running on http://localhost:8001/"
echo "The webssh server is running on http://localhost:8002/ssh/host/127.0.0.1"
echo "Don't press any key or close this window, otherwise the program will stop."

# Wait for user input
read -p "Press any key to continue..."
