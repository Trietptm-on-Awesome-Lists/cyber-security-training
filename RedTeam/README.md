# Read Team

## Disable GUI (Lubuntu IT)
[askubuntu thread](https://askubuntu.com/questions/825094/how-do-i-boot-directly-to-tty1-in-ubuntu)
Edit /etc/default/grub:
```
GRUB_CMDLINE_LINUX_DEFAULT="text"
```

Commands:
```
update-grub
systemctl enable multi-user.target --force
systemctl set-default multi-user.target
```
