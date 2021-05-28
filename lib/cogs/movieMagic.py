import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands

class MovieMagic(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Movie Magic Online")
        print("Movie Magic Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("movieMagic")

    # Command to add movie to database
    @command()
    async def movie(self, ctx, *, message):
        embed=discord.Embed(title=message, description=f'Suggested by {ctx.author}')
        await ctx.send(embed=embed)

    async def printEmbed(self, ctx, *, message):
        embed = discord.RichEmbed(title=message, description=f'Suggested by {ctx.author}')
        embed.setThumbnail(f'{findMoviePoster(message)}')
        await ctx.send(embed=embed)

    async def findMoviePoster(message):
        pass


def setup(bot):
    bot.add_cog(MovieMagic(bot))