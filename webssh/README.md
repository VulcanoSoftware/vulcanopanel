web SSH client:

Web SSH Client using ssh2, socket.io, xterm.js, and express

A bare bones example of an HTML5 web-based terminal emulator and SSH client. We use SSH2 as a client on a host to proxy a Websocket / Socket.io connection to a SSH2 server.

<img width="1044" alt="Screenshot 2017-03-23 18.13.59" src="https://cloud.githubusercontent.com/assets/1668075/24272639/8ad4fef0-0ff4-11e7-8dd0-72b26605e467.png">



  * **kex** - _array_ - Key exchange algorithms.

    * Default values:

      1. ecdh-sha2-nistp256
      2. ecdh-sha2-nistp384
      3. ecdh-sha2-nistp521
      4. diffie-hellman-group-exchange-sha256
      5. diffie-hellman-group14-sha1

    * Supported values:

      * ecdh-sha2-nistp256
      * ecdh-sha2-nistp384
      * ecdh-sha2-nistp521
      * diffie-hellman-group-exchange-sha256
      * diffie-hellman-group14-sha1
      * diffie-hellman-group-exchange-sha1
      * diffie-hellman-group1-sha1

  * **cipher** - _array_ - Ciphers.

    * Default values:

      1. aes128-ctr
      2. aes192-ctr
      3. aes256-ctr
      4. aes128-gcm
      5. aes128-gcm@openssh.com
      6. aes256-gcm
      7. aes256-gcm@openssh.com
      8. aes256-cbc **legacy cipher for backward compatibility, should removed :+1:**

    * Supported values:

      * aes128-ctr
      * aes192-ctr
      * aes256-ctr
      * aes128-gcm
      * aes128-gcm@openssh.com
      * aes256-gcm
      * aes256-gcm@openssh.com
      * aes256-cbc
      * aes192-cbc
      * aes128-cbc
      * blowfish-cbc
      * 3des-cbc
      * arcfour256
      * arcfour128
      * cast128-cbc
      * arcfour

  * **hmac** - _array_ - (H)MAC algorithms.

    * Default values:

      1. hmac-sha2-256
      2. hmac-sha2-512
      3. hmac-sha1 **legacy hmac for backward compatibility, should removed :+1:**

    * Supported values:

      * hmac-sha2-256
      * hmac-sha2-512
      * hmac-sha1
      * hmac-md5
      * hmac-sha2-256-96
      * hmac-sha2-512-96
      * hmac-ripemd160
      * hmac-sha1-96
      * hmac-md5-96

  * **compress** - _array_ - Compression algorithms.

    * Default values:

      1. none
      2. zlib@openssh.com
      3. zlib

    * Supported values:

      * none
      * zlib@openssh.com
      * zlib