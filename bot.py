import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
  print('Bot is online!')

@bot.command()
async def ping(ctx):
  await bot.say('Pong!')
  
@bot.event
async def on_message(message):
    if "(╯°□°）╯︵ ┻━┻" in message.content:
      await bot.send_message(message.channel, "┬─┬﻿ ノ( ゜-゜ノ)")

    await bot.process_commands(message)

bot.run('MzU4MzAwNjE3NjY1NTQ0MTk0.DJ2kbw.YR9Rr0VuHk0vy9B6z_Uu-AT5AWA')
 
