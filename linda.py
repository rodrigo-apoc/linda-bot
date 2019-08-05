#! python3
# -*- coding: utf-8 -*

# Libs
import discord,logging
# Configs
from brainLinda import *
from googlesearch import Google


# log file
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Google instance
Google = Google()

# Discord Client
client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!google'):
		await message.channel.send(Google.search(str(message.content)))
	else:
		await message.channel.send(kernel.respond(message.content))

client.run('your key')