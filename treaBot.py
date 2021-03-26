import discord
import os
import subprocess
from discord.ext import commands

bot_dir=r"C:\Users\Admin\Desktop\ModServer"
assert os.path.isdir(bot_dir)
os.chdir(bot_dir)

client = commands.Bot(command_prefix = '$')
self.stdout = self.get_channel(805177594441629746)

@client.event
async def on_ready():
    print('Trea has Sprouted!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def fuckShitUp(ctx):
    await ctx.send(f'Attempting to launch server. Hope this doesnt break shit')
    subprocess.run([r'start.bat'])



client.run('ODA1MDkwODY5NjgxMzI0MDUy.YBV1TQ.TYU-QFyuNQeV54bDH3xwbsKFFas')