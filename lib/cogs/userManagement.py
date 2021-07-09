import discord
from discord import role

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

class UserManagement(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("User Management Online")
        print("User Management Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("userManagement")

    @command()
    async def addAssignableRole(self, ctx, rolename):
        pass

    @command()
    async def addRole(self, ctx, rolename):
        AddRole = discord.utils.get(ctx.guild.roles, name=rolename)
        if AddRole.name == rolename:
            await ctx.author.add_roles(AddRole)
            await ctx.send(f"{rolename} has been added to {ctx.author}")

def setup(bot):
    bot.add_cog(UserManagement(bot))