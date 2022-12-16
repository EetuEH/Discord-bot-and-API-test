import discord
import os
import random
import json

client = discord.Client()

@client.event
async def on_ready():
    print('Sisäänkirjautuminen käyttäjänä {0.user}'.format(client))



client.run("MTA1MzM2NDI3MDAyMjI4MzM0NA.Gg9k93.ITZqKkxzBPImBqhMydJxxuG4Qi1fZSPIlAxFTw")