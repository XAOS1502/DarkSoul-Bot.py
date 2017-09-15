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
    await ctx.send(embed=em)
    


      await bot.process_commands(message)
if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
