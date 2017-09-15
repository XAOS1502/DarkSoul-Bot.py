import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
  print('Bot is online!')

@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')
  
@bot.event
async def on_message(message):
    if "(╯°□°）╯︵ ┻━┻" in message.content:
      await message.channel.send("┬─┬﻿ ノ( ゜-゜ノ)")

    await bot.process_commands(message)

bot.run(MzU4MzAwNjE3NjY1NTQ0MTk0.DJ3NCQ.MAIyOQ1ntr4bwyqOazVJReLmv6Q)
 
