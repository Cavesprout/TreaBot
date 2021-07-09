import discord

from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands
from datetime import date, datetime
from random import randint

from ..db import db



class LeavesXP(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.numMessages = 0

    async def process_xp(self, message):
        try:
            xp, xpratelimit = db.record("SELECT XP, XPRateLimit FROM userXP WHERE UserID = ?", message.author.id)
        except:
            db.execute("INSERT INTO userXP (UserID) VALUES (?)", message.author.id)
            print(f"{message.author} not found in database. adding to db")
            xp, xpratelimit = db.record("SELECT XP, XPRateLimit FROM userXP WHERE UserID = ?", message.author.id)

        if datetime.fromisoformat(xpratelimit) < datetime.utcnow():
            await self.add_xp(message, xp)

    async def add_xp(self, message, xp):
        xp_to_add = randint(1, 4)

        db.execute("UPDATE userXP SET XP = XP + ?, XPRateLimit = ? WHERE UserID = ?", xp_to_add, datetime.utcnow().isoformat(), message.author.id)
        
        self.numMessages += 1

        if self.numMessages > 10:
            print(f'committed xp database')
            self.numMessages = 0
            db.commit()

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Falling Leaves Online")
        print("Falling Leaves Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("leavesXP")

    @Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            await self.process_xp(message)

    @command(aliases=['bank', 'lb'])
    async def leafbank(self, ctx):
        xp = db.record("SELECT XP FROM userXP WHERE UserID = ?", ctx.message.author.id)
        await ctx.send(f'Hello {ctx.message.author.name}! You have collected {xp[0]} fallen leaves!')

    @command()
    async def glb(self, ctx):
        pass


def setup(bot):
    bot.add_cog(LeavesXP(bot))