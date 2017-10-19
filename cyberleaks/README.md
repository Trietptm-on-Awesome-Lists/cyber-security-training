# CyberLeaks

## How to use

### Server

Define "leaks" folder as root for web server and run "server.py" at boot with crontab or similar. For prettier directory theme, install: http://adamwhitcroft.com/apaxy/

Example crontab line:

```
@reboot python3 /path/to/server.py
```

Example apache2 web server conf /etc/apache2/sites-available/000-default.conf:

```
<VirtualHost *:80>

    ServerName cyberleaks.com
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/cyberleaks/leaks

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

### Client

Example line:

```
python3 client.py /path/to/leak_file
```
