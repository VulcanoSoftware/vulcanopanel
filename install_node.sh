#!/bin/sh
# installs fnm (Fast Node Manager)
$ curl -fsSL https://fnm.vercel.app/install | bash

# activate fnm
$ source ~/.bashrc

# download and install Node.js
$ fnm use --install-if-missing 20

# verifies the right Node.js version is in the environment
$ node -v # should print `v20.17.0`

# verifies the right npm version is in the environment
$ npm -v # should print `10.8.2`