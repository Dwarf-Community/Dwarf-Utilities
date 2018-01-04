import discord
from discord.ext import commands
import aiohttp

from .controller import UtilitiesController


class Utilities:
    """Useful commands that serve multiple purposes."""

    def __init__(self, bot):
        self.bot = bot
        self.utilities = UtilitiesController()
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.clock = self.bot.subcommand(command_group='set')(self.clock)
    
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
    async def clock(self, ctx, *, time):
        utc_offset = utilities.calculate_utc_offset(time)
        utilities.save_utc_offset(ctx.message.author, utc_offset)
        await ctx.send("Done.")


def setup(bot):
    bot.add_cog(Utilities(bot))
