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
        self.activeServer = None
        self.activeServerName = None

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Minecraft Controller Online")
        print("Minecraft Controller Online")

        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("minecraftController")

    @command(aliases=['launch', 'launchserver'])
    async def launchServer(self, ctx, server):
        if (self.activeServer != None):
            await ctx.send(f'A server is already running')
        else:
            await ctx.send(f'Attempting to launch server: {server}')
            server_dir = os.path.join('MinecraftServers', f'{server}')
            assert os.path.isdir(server_dir)
            env = dict(os.environ)
            env['JAVA_OPTS'] = 'foo'
            self.activeServer = subprocess.Popen(['java', '-server', '-Xmx6G', '-Xms6G', '-jar', f'{server}-launch.jar'], env=env, cwd=server_dir)
            self.activeServerName = server

    @command(aliases=['kill'])
    async def killServer(self, ctx):
        if (self.activeServer != None):
            await ctx.send(f'Attempting to kill server: {self.activeServerName}')
            self.activeServer.terminate()
            self.activeServer = None
            self.activeServerName = None
        else:
            await ctx.send(f'There is no server running')

    @command(aliases=['list', 'listservers'])
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

    @command(aliases=['active', 'activeservers'])
    async def activeServers(self, ctx):
        if (self.activeServer != None):
            await ctx.send(f'The current active server is: {self.activeServerName}')
        else:
            await ctx.send(f'There is no server running')
        

def setup(bot):
    bot.add_cog(MinecraftController(bot))
