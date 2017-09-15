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
        em.description = f"{self.ws.latency * 1000:.4f} ms"
        em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
        await ctx.send(embed=em)
        
@bot.event
async def on_message(message):
    if "(╯°□°）╯︵ ┻━┻" in message.content:
      await message.channel.send("┬─┬﻿ ノ( ゜-゜ノ)")

    await bot.process_commands(message)
if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
