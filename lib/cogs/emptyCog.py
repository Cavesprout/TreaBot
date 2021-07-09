import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

class EC(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("EC Online")
        print("EC Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("emptyCog")



def setup(bot):
    bot.add_cog(EC(bot))