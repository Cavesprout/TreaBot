import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands


class TwitCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Flagrant Narcissism Online")
        print("Flagrant Narcissism Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("twitterCog")

    @command()
    async def twitping(self, ctx):
        await ctx.send(f'Pong! ({round(self.bot.latency * 1000)} ms)')


def setup(bot):
    bot.add_cog(TwitCog(bot))