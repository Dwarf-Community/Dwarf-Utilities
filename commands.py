import discord
from discord.ext import commands

from dwarf import permissions
# from dwarf import formatting as f
from dwarf.bot import subcommand, send_command_help
from .api import UtilitiesAPI


utilities = UtilitiesAPI()


class Utilities:
    """Useful commands that serve multiple purposes."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
    
    @commands.command(pass_context=True, hidden=True)
    @permissions.owner()
    async def say(self, ctx, *, message, channel_id=None):
        if channel is None:
            await self.bot.say(message)
        else:
            destination = await self.bot.get_channel(channel_id)
            await self.bot.send_message(destination, message)
            await self.bot.say("Done.")
    
    @commands.command(pass_context=True)
    @subcommand(command_group='set')
    async def clock(self, ctx, *, time):
        utc_offset = utilities.calculate_utc_offset(time)
        utilities.save_utc_offset(ctx.message.author, utc_offset)
        await self.bot.say("Done.")
