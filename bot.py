import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
  print('Bot is online!')

@bot.command(name='presence')
async def _set(Type=None,*,thing=None):
    """Change the bot's discord game/stream!"""
    if Type is None:
            await bot.say('Usage: `.presence [game/stream] [message]`')
    else:
        if Type.lower() == 'stream':
            await bot.change_presence(game=discord.Game(name=thing,type=1,url='https://www.twitch.tv/a'),status='online')
            await bot.say('Set presence to. `Streaming {}`'.format(thing))
        elif Type.lower() == 'game':
            await bot.change_presence(game=discord.Game(name=thing))
            await bot.say('Set presence to `Playing {}`'.format(thing))
        elif Type.lower() == 'clear':
            await bot.change_presence(game=None)
            await bot.say('Cleared Presence')
        else:
            await bot.say('Usage: `.presence [game/stream] [message]`')
  
  @bot.command()
async def ping(ctx):
    """Pong! Returns your websocket latency."""
    em = discord.Embed()
    em.title ='Pong! Websocket Latency:'
    em.description = f"{bot.ws.latency * 1000:.4f} ms"
    await ctx.send(embed=em)
    

@bot.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=358300617665544194&scope=bot&permissions=66186303')
    



if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
