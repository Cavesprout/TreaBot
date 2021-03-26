import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

import subprocess

class MinecraftController(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Minecraft Controller Online")
        print("Minecraft Controller Online")

        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("minecraftController")

    @command()
    async def launchServer(self, ctx):
        await ctx.send(f'Attempting to launch server.')
        subprocess.run([r'start.bat'])


def setup(bot):
    bot.add_cog(MinecraftController(bot))