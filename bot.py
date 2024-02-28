# written by niklas k
import os
import docker
import discord
from dotenv import load_dotenv

load_dotenv()
# set token in .env file with attribute DISCORD_TOKEN, MESSAGE_CHANNEL and LISTEN_CHANNEL
TOKEN = os.getenv('DISCORD_TOKEN')
channel_message = int(os.getenv('MESSAGE_CHANNEL'))
channel_listen = int(os.getenv('LISTEN_CHANNEL'))
prefix = os.getenv('COMMAND_PREFIX')
dockerClient = docker.from_env()
serverContainer = dockerClient.containers.get("sun_asa_server")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/" + prefix + " help"))

    async def on_message(self, message):
        # the channel the bot answers in
        channel = client.get_channel(channel_message)
        # the channel the bot listens in
        if message.channel.id == channel_listen:
            if (message.content == "/" + prefix + " help"):
                await channel.send(f'Folgende Commands stehen zur Verfügung: ```\n/' + prefix + ' start\n/' + prefix + ' stop\n/' + prefix + ' status\n/' + prefix + ' backup\n```')
            elif (message.content == "/" + prefix + " start"):
                await channel.send(f'{message.author.mention} Alles klar, ich geb mein bestes....')
                if (serverContainer.status == "exited"):
                    serverContainer.start()
                    await channel.send(f'Der Container war gestoppt, also starte ich ihn erstmal neu. Der Server sollte in 3-5 Minuten online sein.')
                else:
                    res = serverContainer.exec_run("manager update")
                    await channel.send(f'```\nDer Server sollte in ein paar Minuten online sein.\n```')
            elif (message.content == "/" + prefix + " stop"):
                await channel.send(f'{message.author.mention} Mal schauen ob der Bro gestoppt werden kann.')
                if (serverContainer.status == "exited"):
                    await channel.send(f'Der Server ist bereits gestoppt.')
                else:
                    res = serverContainer.exec_run("manager stop")
                    await channel.send(f'Der Server wurde gestoppt. ```\n{res[1]}\n```')
            elif (message.content == "/" + prefix + " status"):
                await channel.send(f'{message.author.mention} Uno Momento! Ich frag mal ganz lieb nach dem Status.')
                if (serverContainer.status == "exited"):
                    await channel.send(f'Der Container laeuft nicht.')
                else:
                    res = serverContainer.exec_run("manager status --full")
                    await channel.send(f'```\n{res[1]}\n```')
            elif (message.content == "/" + prefix + " backup"):
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
