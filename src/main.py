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



client.run(token)