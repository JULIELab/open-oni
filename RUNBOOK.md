The hetzner cloud instance where romantik-zeitungen.de is hosted has 4 vcpus, 16GB RAM and 160GB of disc space.

# Firewall

Currently there is a redirect from port 80 to the unprivileged port 8080 where either the open-oni web container
(with the AMZ portal) is listening, or the Python 3 built-in web server (-m http.server) is serving
the static maintenance site (/home/open-oni/wartung/index.html).
Binding to the unprivileged port can be done as the user *open-oni* and doesn't need root's capabilities!

```
# cat /root/iptables-8080to80.sh 
#! /usr/bin/env bash

iptables -A INPUT -i eth0 -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --dport 8080 -j ACCEPT
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
```

**Only root is allowed to set these rules!**

# Custom AMZ Helper Scripts

/home/open-oni/**amz-up-{production|dev}.sh** are just primitive wrappers around the usual **docker-compose up -d**
where the necessary environment variables are getting set. 

# Maintenance Site
/home/open-oni/**maintenance.sh** is just a wrapper that runs the Python 3 built-in web server with the correct port settings
and changes to the subdirectory *maintenance* to serve **any** files there

# Switching to maintenance mode
1. call **amz-down-production.sh** to stop all containers and unset all unneeded variables (wraps docker-compose down, unset)
2. call **maintenance.sh**, preferably in a *tmux session*

# Running AMZ
1. Stop/kill the maintenance site's python server; if it's running in a tmux session, join that via *tmux a* and stop it there
2. call **amz-up-production.sh** to start open-oni's containers with the correct environment variables

# TODO: implement the following functionallity:
# Testing AMZ
1. for testing purposes call **amz-up-dev.sh** to run a second portal instance, without all the batches, on port 8082
2. after testing call **amz-down-dev.sh** to stop the second portal instance and unset all unnecessary environment variables
