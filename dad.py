import discord
from discord.ext import commands
import asyncio
import secrets
import re

bot = discord.Client()
check = ["im","i'm","Im","I'm","iM","i'M","IM","I'M","i am","I am","I aM","I Am","i AM","I AM"] #lol

@bot.event
async def on_ready():
    print('Bot....but he is admin')
    version = discord.__version__
    print(version)

@bot.event
async def on_message(message):
    #channel = bot.get_channel(secrets.channel)
    msg = message.content
    msgcheck = msg.lower()
    botauthor = message.author.bot
    if botauthor: #bot must ignore it's own messages
        pass
    else:
        for i in range(14):
            if msg.startswith(check[i]):
                newmsg = re.sub(check[i],'',msg)
                #newmsg = re.sub(check[i].lower(),'',newmsg)
                #newmsg = re.sub(check[i].swapcase(),'',newmsg)
                reply = 'Hi' + newmsg + ', my name is dad!'
                await message.channel.send(str(reply))
        else:
            pass

    #await bot.process_commands(message) #allows extra commands to run

bot.run(secrets.token)
