Service File for systemctl: 

Path: /etc/systemd/system/name.service
```
[Unit]
Description=Discord Bot fuer den ARK Server
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /etc/ark/arkbot/bot.py
[Install]
WantedBy=multi-user.target
```
