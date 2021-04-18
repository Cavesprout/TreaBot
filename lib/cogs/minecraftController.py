import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

import os
import subprocess
import psutil

class MinecraftController(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Minecraft Controller Online")
        print("Minecraft Controller Online")

        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("minecraftController")

    @command(aliases=['launch', 'launchserver'])
    async def launchServer(self, ctx):
        await ctx.send(f'Attempting to launch server.')
        self.p = subprocess.Popen([r'start.bat'], shell=True)

    @command()
    async def killServer(self, ctx):
        await ctx.send(f'Attempting to kill server.')
        await ctx.send(f'This command is currently broken')

def setup(bot):
    bot.add_cog(MinecraftController(bot))