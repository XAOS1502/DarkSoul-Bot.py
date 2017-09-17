import discord
from discord.ext import commands
from urllib.parse import urlparse
import datetime
import asyncio
import random
import pip
import os
import io


class Mod:

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        '''Kick someone from the server.'''
        try:
            await ctx.guild.kick(member, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, member, success, 'kick')

        await ctx.send(embed=emb)
