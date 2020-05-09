#Oracle Bot by underSFX

import os
import discord
from discord.ext import commands
from senderscore import senderscore

TOKEN = os.environ['DISCORD_TOKEN']

client = commands.Bot(command_prefix = '.')

# STARTUP
@client.event
async def on_ready():
    print('Bot is ready!')


# COMMANDS
@client.command()
async def echo(*args):
    print('echo call with args:', args)
    await client.say(' '.join(args))


@client.command()
async def score(ip):
    print('senderscore call with arg:', ip)
    if not senderscore.is_valid_ip(ip):
        await client.say('"{}" não é um ip valido'.format(ip))
        return

    ip_score = senderscore.get_score(ip)

    if not ip_score:
        await client.say('"{}" atualmente não tem um senderscore atrelado'.format(ip))
    else:
        await client.say('"{}" atualmente tem o senderscore: {}'.format(ip, ip_score))


# EVENTS
# @client.event
# async def on_message_delete(message):
#     print('Mensagem Deletada: {}: {}'.format(message.author, message.content))


client.run(TOKEN)
