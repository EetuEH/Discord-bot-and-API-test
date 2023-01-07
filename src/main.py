import discord
import os
import random
import json

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        data = json.load(f)
else:
    template = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(template, f)

token = data["Token"]
prefix = data["Prefix"]

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Sisäänkirjautuminen käyttäjänä {0.user}'.format(client))

@client.event
async def on_message(message):
    print(str(message.content))
    #varmistetaan, ettei botti reagoi omiin viesteihinsä
    if message.author == client.user:
        return

    username = str(message.author)
    user_msg = str(message.content)
    channel = str(message.channel)

    #lähettää botin viiveen viestinä muodossa "x millisekuntia"
    if (user_msg[0] == prefix & user_msg[1:] == "ping"):
            print("viive pyydetty")
            #muutetaan viive sekunneista millisekunneiksi ja pyöristetään yhden numeron tarkkuudella
            viive = round(client.latency * 1000, 1)
            await message.channel.send(f"Pong! {viive}ms")

client.run(token)