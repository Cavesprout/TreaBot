import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands


class BasicCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Basic Functions Online")
        print("Basic Functions Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("basicCog")

    @command()
    async def twitping(self, ctx):
        await ctx.send(f'Pong! ({round(self.bot.latency * 1000)} ms)')


def setup(bot):
    bot.add_cog(BasicCog(bot))