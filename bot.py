# written by niklas k
import os
import docker
import discord
from dotenv import load_dotenv

load_dotenv()
# set token in .env file with attribute DISCORD_TOKEN
TOKEN = os.getenv('DISCORD_TOKEN')
channel_message = os.getenv('MESSAGE_CHANNEL')
channel_listen = os.getenv('LISTEN_CHANNEL')
dockerClient = docker.from_env()
serverContainer = dockerClient.containers.get("sun_asa_server")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/server help"))

    async def on_message(self, message):
        # the channel the bot answers in
        channel = client.get_channel(channel_message)
        # the channel the bot listens in
        if message.channel.id == channel_listen:
            if (message.content == "/server help"):
                await channel.send(f'Folgende Commands stehen zur Verfügung: ```\n/server start\n/server stop\n/server status\n/server backup\n```')
            elif (message.content == "/server start"):
                await channel.send(f'{message.author.mention} Alles klar, ich geb mein bestes....')
                if (serverContainer.status == "exited"):
                    serverContainer.start()
                    await channel.send(f'Der Container war gestoppt, also starte ich ihn erstmal neu. Der Server sollte in 3-5 Minuten online sein.')
                else:
                    res = serverContainer.exec_run("manager update")
                    await channel.send(f'```\nDer Server sollte in ein paar Minuten online sein.\n```')
            elif (message.content == "/server stop"):
                await channel.send(f'{message.author.mention} Mal schauen ob der Bro gestoppt werden kann.')
                if (serverContainer.status == "exited"):
                    await channel.send(f'Der Server ist bereits gestoppt.')
                else:
                    res = serverContainer.exec_run("manager stop")
                    await channel.send(f'Der Server wurde gestoppt. ```\n{res[1]}\n```')
            elif (message.content == "/server status"):
                await channel.send(f'{message.author.mention} Uno Momento! Ich frag mal ganz lieb nach dem Status.')
                if (serverContainer.status == "exited"):
                    await channel.send(f'Der Container laeuft nicht.')
                else:
                    res = serverContainer.exec_run("manager status --full")
                    await channel.send(f'```\n{res[1]}\n```')
            elif (message.content == "/server backup"):
                await channel.send(f'{message.author.mention} Backup wird erstellt.')
                if (serverContainer.status == "exited"):
                    await channel.send(f'Der Container läuft nicht.')
                else:
                    res = serverContainer.exec_run("manager backup")
                    await channel.send(f'```\n{res[1]}\n```')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
