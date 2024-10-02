#!/bin/bash

# Change directory to linux
cd linux

# Run installation scripts
./install_ssh.sh
./install_sftp.sh

# Open the specified ports in the firewall
sudo ufw allow 4340/tcp
sudo ufw allow 2222/tcp
sudo ufw reload

# Display network configuration
ip addr

# Display server information
echo "The sftp server is running on http://localhost:4340/"
echo "The webssh server is running on http://localhost:2222/ssh/host/127.0.0.1"
echo "Don't press any key or close this window, otherwise the program will stop."

# Wait for user input
read -p "Press any key to continue..."
