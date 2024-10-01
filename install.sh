#!/bin/sh
$ ls
$ cd webssh
$ npm install --production
$ npm start
$ ifconfig
echo "the webssh server is running on http://localhost:2222/ssh/host/127.0.0.1"
$ cd ..
$ ls
$ cd sftp_web_client
$ npm install --production
$ ./wfc start
$ ifconfig
echo "the webssh server is running on http://localhost:4340/"