#!/bin/bash

# Controleer of OpenSSH is geïnstalleerd
if ! systemctl is-active --quiet sshd; then
    echo "OpenSSH is niet geïnstalleerd. Aan het installeren..."
    if sudo pacman -S --noconfirm openssh; then
        echo "OpenSSH is succesvol geïnstalleerd."
    else
        echo "Fout bij het installeren van OpenSSH. Controleer je systeeminstellingen."
        exit 1
    fi
else
    echo "OpenSSH is al geïnstalleerd."
fi

# Start de SSH-server
echo "De SSH-server wordt gestart..."
sudo systemctl start sshd

# Controleer of firewalld actief is
if systemctl is-active --quiet firewalld; then
    # Controleer of de regel voor poort 22 bestaat en voeg deze toe als dat niet zo is
    if ! sudo firewall-cmd --list-all | grep -q '22/tcp'; then
        echo "Poort 22 wordt geopend in de firewall..."
        sudo firewall-cmd --add-port=22/tcp --permanent
        sudo firewall-cmd --reload
        echo "Poort 22 is geopend."
    else
        echo "Poort 22 is al open in de firewall."
    fi
else
    echo "firewalld is niet actief. Start firewalld en probeer het opnieuw."
    exit 1
fi

echo "SSH/SFTP-server is gestart."
