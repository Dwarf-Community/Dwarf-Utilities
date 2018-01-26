import discord
from discord.ext import commands
import aiohttp

from .controller import UtilitiesController
from dwarf.bot import Cog


class Utilities(Cog):
    """Useful commands that serve multiple purposes."""

    def __init__(self, bot, extension):
        super().__init__(bot, extension)
        self.utilities = UtilitiesController()

    @commands.is_owner()
    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel, *, message):
        
        await channel.send(message)
        await ctx.send("Your message has been sent.")
    
    @commands.is_owner()
    @commands.command()
    async def dm(self, ctx, user: discord.User, *, message):
        
        await user.send(message)
        await ctx.send("Your message has been sent.")
    
    @commands.command()
    async def set_clock(self, ctx, *, time):
        utc_offset = utilities.calculate_utc_offset(time)
        utilities.save_utc_offset(ctx.message.author, utc_offset)
        await ctx.send("Done.")
