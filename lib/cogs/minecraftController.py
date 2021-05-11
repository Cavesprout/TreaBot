import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

import os
import signal
import subprocess
import psutil

bot_dir=r"C:\Users\Admin\Desktop\Trea"

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
    async def launchServer(self, ctx, server):
        await ctx.send(f'Attempting to launch server: {server}')
        server_dir = os.path.join('MinecraftServers', f'{server}')
        assert os.path.isdir(server_dir)
        env = dict(os.environ)
        env['JAVA_OPTS'] = 'foo'
        self.activeServer = subprocess.Popen(['java', '-Xmx4096M', '-Xms4096M', '-jar', f'{server}-launch.jar'], env=env, cwd=server_dir)


    @command()
    async def killServer(self, ctx):
        await ctx.send(f'Attempting to kill server.')
        self.activeServer.terminate()

    @command()
    async def listServers(self, ctx):
        dirs = os.listdir('MinecraftServers')
        
        for d in dirs:
            print(f'{d} directory found.')
            try:
                path = f"MinecraftServers\{d}\serverinfo.txt"
                print(f'Accessing {path}')
                f = open(path)
                # Do something with the file
                await ctx.send(f'{d} directory accessed.')
            except IOError:
                print("File not accessible")

def setup(bot):
    bot.add_cog(MinecraftController(bot))
