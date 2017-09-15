import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
  print('Bot is online!')

@bot.command()
async def ping(ctx):
    """Pong! Returns your websocket latency."""
    em = discord.Embed()
    em.title ='Pong! Websocket Latency:'
    em.description = f"{bot.ws.latency * 1000:.4f} ms"
    em.color = discord.colour.green()
    await ctx.send(embed=em)
        
@bot.event
async def on_message(message):
    if "(╯°□°）╯︵ ┻━┻" in message.content:
      await message.channel.send("┬─┬﻿ ノ( ゜-゜ノ)")

@bot.command(pass_context=True)
async def ping(ctx):
    """Pong! Check your response time."""
    msgtime = ctx.message.timestamp.now()
    await (await bot.ws.ping())
    now = datetime.datetime.now()
    ping = now - msgtime
    pong = discord.Embed(title='Pong! Response Time:',
    					 description=str(ping.microseconds / 1000.0) + ' ms',
                         color=0x00ffff)
    await bot.say(embed=pong)


      await bot.process_commands(message)
if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
