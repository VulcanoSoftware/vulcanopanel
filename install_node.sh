#!/bin/bash

# Installs fnm (Fast Node Manager) via curl
curl -fsSL https://fnm.vercel.app/install | bash

# Activate fnm by adding it to the PATH
# This might require restarting your terminal or sourcing your profile
# Uncomment and adjust the line below if necessary
# export PATH="$HOME/.fnm:$PATH"

# Download and install Node.js version 20 using fnm
fnm install 20
fnm use 20

# Verifies the right Node.js version is in the environment
node -v

# Verifies the right npm version is in the environment
npm -v

read -p "Press any key to continue..."
