#!/bin/bash

# Check if OpenSSH is installed
if ! systemctl is-active --quiet sshd; then
    echo "OpenSSH is not installed. Installing..."
    if sudo dnf install -y openssh-server; then
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
sudo systemctl enable sshd  # Enable SSH to start on boot

# Check if the firewall rule for port 22 exists and create it if it does not
if ! sudo firewall-cmd --list-all | grep -q '22/tcp'; then
    echo "Opening port 22 in the firewall..."
    sudo firewall-cmd --permanent --add-port=22/tcp
    sudo firewall-cmd --reload
    echo "Port 22 has been opened."
else
    echo "Port 22 is already open in the firewall."
fi

echo "SSH/SFTP server has started."
