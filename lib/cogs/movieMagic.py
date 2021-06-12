import discord
import aiohttp

from aiohttp import request
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands
from lib import bot

from lib.bot import botsecrets

class MovieMagic(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ltResponse = None

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Movie Magic Online")
        print("Movie Magic Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("movieMagic")

    @command(aliases=['movielookup', 'lookup'])
    async def movieLookup(self, ctx, *, message):
        url = botsecrets["IMDBURL"]
        querystring = {"q":f"{message}"}
        headers= {
            'x-rapidapi-key': botsecrets["x-rapidapi-key"],
            'x-rapid-host': botsecrets["x-rapidapi-host"]
        }
        async with aiohttp.ClientSession() as session:
            async with await session.get(url=url, headers=headers, params=querystring) as response:
                if (response.status != 200):
                    await ctx.send(f"Error Code: {response.status}")
                    return
                print(response.text)
                print(response._body)
                
                self.ltResponse = response

            


    # Command to add movie to database
    @command()
    async def movie(self, ctx, *, message):
        embed=discord.Embed(title=message, description=f'Suggested by {ctx.author}')
        await ctx.send(embed=embed)

    async def printEmbed(self, ctx, *, message):
        embed = discord.RichEmbed(title=message, description=f'Suggested by {ctx.author}')
        embed.setThumbnail(f'sample URL')
        await ctx.send(embed=embed)

    async def findMoviePoster(message):
        pass


def setup(bot):
    bot.add_cog(MovieMagic(bot))