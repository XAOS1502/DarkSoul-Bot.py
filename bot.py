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

bot.run()
 
