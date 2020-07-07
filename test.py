import discord
from discord.ext import commands
import asyncio
import secrets
import re

bot = discord.Client()
check = ['im','i am',"i'm"]

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
    for i in range(3):
        if msgcheck.startswith(check[i]):
            newmsg = re.sub(check[i],'',msg)
            reply = 'Hi' + newmsg + ', im dad!'
            await message.channel.send(str(reply))

    #await bot.process_commands(message) #allows extra commands to run

bot.run(secrets.token)
