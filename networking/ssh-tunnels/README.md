## Guide to SSH Tunnels
[Article](https://robotmoon.com/ssh-tunnels/)

### SSH command line tags
```shell
-f  # forks the ssh process into the background
-n  # prevents reading from STDIN
-N  # do not run remote commands, use when only forwarding ports
-T  # Disable TTY allocation

ssh -fnNT -L 127.0.0.1:8080:example.org:80 ssh-server
```

### Port Forwarding
Forward a port from one system to another

- **Local port forwarding**  
  Allows to forward traffic on the SSH client to some destination through
  an SSH server. To use secure connection to access remote services that
  communicates using plain text. Ex: redis. You can use this instead of
  exposing them to public internet.

  ```shell
  ssh -L 127.0.0.1:8080:example.org:80 ssh-server

  # from the prespective of example.org traffic originates from ssh-server
  ```

  ```shell
  ssh -L 192.168.0.1:5432:127.0.0.1:5432 ssh-server
  
  # Forwards connections to 192.168... on your local system to localhost
  # on ssh-server
  ```
  - SSH configuration
    - Enable port forwarding (default yes)
      ```
      // on /etc/ssh/sshd_config

      AllowTcpForwarding yes

      // If you are forwarding ports on interfaces other than localhost then
      // you need to enable GatewayPorts on your local system

      GatewayPorts yes
      ```

- **Remove port forwarding**  
  Forward traffic on a SSH server to a destination server through either the
  SSH client or another remote host. This give users on public network access
  to resources on public network.
  - Making a local development server available on public network
  - Granting IP-restricted access to a remote resource on a private network

  ```shell
  ssh -R 8080:localhost:80 ssh-server

  # Traffic of 8080 on ssh-server to 80 of your local
  ```

  ```shell
  ssh -R 1.2.3.4:8080:localhost:80 ssh-server

  # Forward traffic to ssh-server:8080 to local 80 on your system while
  # only allowing access to ssh tunnel entrance on ssh-server from IP address
  # 1.2.3.4.The GatewayPorts clientspecified directive with this.
  ```

  ```shell
  ssh -R 8080:example.org:80 ssh-server

  # Forwards traffice to all interfaces on ssh-server:8080 to local 80 on your
  # system. From your local system traffice is then forwarded to example.org:80
  ```

  - SSH server configuration.  
    By default, forwarded ports are not accessible to public internet, you need
    to add this to your sshd config on your remote server to forward public
    internet traffic to your local computer.
    ```
    GatewayPorts yes
    ```
    Or if you like to specify which clients are allowed access, you can use
    this on your sshd config instead
    ```
    GatewayPorts clientspecified
    ```

- **Dynamic port forwarding**  
  Opens a SOCKS proxy on the SSH client that let's you forward TCP traffic
  through the SSH server on a remote host. Forwards traffic from a range of ports
  to a remote server.

  ```shell
  ssh -D 3000 ssh-server
  ```

- **Forwarding from privileged ports**
  To use a privileged port (ports 1 - 1023) to forward traffic, you'll need
  to run SSH with superuser privileges on the system that opens the port
  ```shell
  sudo ssh -L 80:example.com:80 ssh-server
  ```

 
