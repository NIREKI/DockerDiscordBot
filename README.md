# Discord bot for controlling an ASA Docker Server

1. `git clone https://github.com/NIREKI/DiscordDockerRemote.git`
2. Change directory `cd DiscordDockerRemote`
3. Edit `example.env` with your own tokens and id's
4. Rename `example.env to .env` e.g. with `mv example.env .env`
5. Setup the Linux Service according to the following description:

Service file for systemctl: 

Path: /etc/systemd/system/*name*.service
```
[Unit]
Description=*Discord Bot fuer den ARK Server*
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 */etc/ark/arkbot/bot.py*
[Install]
WantedBy=multi-user.target
```

1. Put the file there for the service to work properly
2. Remember to change the path, the name and the description
3. Use `sudo systemctl daemon-reload` to reload the services
4. Start and enable with `sudo systemctl start *name*.service` and `sudo systemctl enable *name*.service`
5. Check status with `sudo systemctl status *name*.service`
