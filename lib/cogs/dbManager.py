import discord

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command

class dbManager(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Database Manager Online")
        print("Database Manager Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("dbManager")

    @command()
    async def pingdb(self, ctx):
        await ctx.send(f'Pong! ({round(self.bot.latency * 1000)} ms)')


def setup(bot):
    bot.add_cog(dbManager(bot))