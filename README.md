# Discord bot for controlling an ASA Docker Server

Only works with [ARK Ascended Docker image by azixus](https://github.com/azixus/ARK_Ascended_Docker)!

1. `git clone https://github.com/NIREKI/DockerDiscordBot.git`
2. Change directory `cd DockerDiscordBot`
3. Install Python3 Dependencies with `pip3 install -r requirements.txt `. Make sure Python3 and Pip3 are installed.
   1. If that shouldn't work, manually install the dependencies [discord.py](https://pypi.org/project/discord.py/), [docker](https://pypi.org/project/docker/) and [python-dotenv](https://pypi.org/project/python-dotenv/)
4. Edit `example.env` with your own token, id's, container name and prefix
5. Rename `example.env to .env` e.g. with `mv example.env .env`
6. Setup the Linux Service according to the following description:


## Setup Linux Service for systemctl

### Servicefile:
Path: /etc/systemd/system/*name*.service
```
[Unit]
Description=*Discord Bot fuer den ARK Server*
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 */etc/ark/DockerDiscordBot/bot.py*
[Install]
WantedBy=multi-user.target
```

1. Put the file there for the service to work properly
2. Remember to change the path, the name and the description
3. Use `sudo systemctl daemon-reload` to reload the services
4. Start and enable with `sudo systemctl start *name*.service` and `sudo systemctl enable *name*.service`
5. Check status with `sudo systemctl status *name*.service`
