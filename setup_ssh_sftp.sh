#!/bin/bash

# Check if OpenSSH is installed
if ! systemctl is-active --quiet sshd; then
    echo "OpenSSH is not installed. Installing..."
    if sudo apt-get install -y openssh-server; then
        echo "OpenSSH has been successfully installed."
    else
        echo "Error installing OpenSSH. Please check your system settings."
        exit 1
    fi
else
    echo "OpenSSH is already installed."
fi

# Start the SSH server
echo "Starting the SSH server..."
sudo systemctl start sshd

# Check if the firewall rule for port 22 exists and create it if it does not
if ! sudo ufw status | grep -q '22/tcp'; then
    echo "Opening port 22 in the firewall..."
    sudo ufw allow 22/tcp
    echo "Port 22 has been opened."
else
    echo "Port 22 is already open in the firewall."
fi

echo "SSH/SFTP server has started."
