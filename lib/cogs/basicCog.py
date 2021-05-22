import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

from glob import glob
import os

COGS = [path.split("\\")[-1][:-3] for path in glob("TreaBot/lib/cogs/*.py")]

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
    async def ping(self, ctx):
        await ctx.send(f'Pong! ({round(self.bot.latency * 1000)} ms)')

    @command()
    async def reloadcogs(self, ctx):
        for cog in COGS:
            self.bot.reload_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog root reloaded")

        print("all cog roots reloaded")
        await ctx.send(f'All cogs have been reloaded.')

    @command()
    async def botdir(self, ctx):
        await ctx.send(f'{os.getcwd()}')


def setup(bot):
    bot.add_cog(BasicCog(bot))