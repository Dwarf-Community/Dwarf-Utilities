import discord
from discord.ext import commands

from dwarf import permissions
# from dwarf import formatting as f
from dwarf.bot import subcommand, send_command_help
from .api import UtilitiesAPI

import aiohttp


utilities = UtilitiesAPI()


class Utilities:
    """Useful commands that serve multiple purposes."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
    
    @commands.command(pass_context=True, hidden=True)
    @permissions.owner()
    async def say(self, ctx, channel : discord.Channel, *, message):
        await self.bot.send_message(channel, message)
        await self.bot.say("Your message has been sent.")
    
    @subcommand(command_group='set')
    @commands.command(pass_context=True)
    async def clock(self, ctx, *, time):
        utc_offset = utilities.calculate_utc_offset(time)
        utilities.save_utc_offset(ctx.message.author, utc_offset)
        await self.bot.say("Done.")


def setup(bot):
    bot.add_cog(Utilities(bot))
