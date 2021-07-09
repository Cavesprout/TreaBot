import discord

from discord.ext.commands import Cog, Greedy
from discord.ext.commands import command
from discord.ext import commands

from ..db import db

import random

class LeafGames(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.broketext = "You don't have enough leaves for that, you broke bitch."

    @Cog.listener()
    async def on_ready(self):
        await self.bot.stdout.send("Leaf Games Online")
        print("Leaf Games Online")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("basicCog")

    @command(aliases=['wheel', 'lw'])
    async def leafwheel(self, ctx, bet):
        numleaves = db.record("SELECT XP FROM userXP WHERE UserID = ?", ctx.author.id)
        if (numleaves[0] >= int(bet)):
            await ctx.send(f"Placing a bet on the Wheel of Leaves for {bet}!!!")
            numChoice = random.randint(1,8)
            spinner = "lol"
            winnings = int(bet)
            if numChoice == 1:
                winnings *= 0.1
                spinner = ":arrow_lower_left:"
            elif numChoice == 2:
                winnings *= 0.2
                spinner = ":arrow_left:"
            elif numChoice == 3:
                winnings *= 0.3
                spinner = ":arrow_down:"
            elif numChoice == 4:
                winnings *= 0.5
                spinner = ":arrow_lower_right:"
            elif numChoice == 5:
                winnings *= 1.2
                spinner = ":arrow_right:"
            elif numChoice == 6:
                winnings *= 1.5
                spinner = ":arrow_upper_left:"
            elif numChoice == 7:
                winnings *= 1.7
                spinner = ":arrow_up:"
            elif numChoice == 8:
                winnings *= 2.4
                spinner = ":arrow_upper_right:"

            winnings = int(winnings)

            embed=discord.Embed(title=f"You won {winnings} leaves!")
            embed.add_field(name=f"1.5----1.7----2.4\n0.2---[{spinner}]---1.2\n0.1----0.3----0.5", value="thanks for playing loser", inline=False)
            await ctx.send(embed=embed)

            delta = int(winnings) - int(bet)

            db.execute("UPDATE userXP SET XP = XP + ? WHERE UserID = ?", delta, ctx.author.id)
            db.execute("UPDATE userXP SET XP = XP + ? WHERE UserID = 69", -delta)

        else:
            await ctx.send(self.broketext)

    @command(aliases=['flip', 'lf'])
    async def leafflip(self, ctx, bet, wager):
        win = False
        numleaves = db.record("SELECT XP FROM userXP WHERE UserID = ?", ctx.author.id)
        if (numleaves[0] > int(bet)):
            if wager == "h" or wager == "t":

                numChoice = random.randint(0,1)
                if (numChoice == 0):
                    if (wager == "h"):
                        await ctx.send(f"The leaf landed on heads! You doubled your bet to {int(bet)*2}!")
                        win = True
                    elif (wager == "t"):
                        await ctx.send(f"The leaf landed on heads, nerd. You lost {int(bet)} leaves.")
                        win = False
                elif (numChoice == 1):
                    if (wager == "t"):
                        await ctx.send(f"The leaf landed on tails! You doubled your bet to {int(bet)*2}!")
                        win = True
                    elif (wager == "h"):
                        await ctx.send(f"The leaf landed on tails, nerd. You lost {int(bet)} leaves.")
                        win = False

                if (win):
                    delta = int(bet)
                else:
                    delta = -int(bet)

                db.execute("UPDATE userXP SET XP = XP + ? WHERE UserID = ?", delta, ctx.author.id)
                db.execute("UPDATE userXP SET XP = XP + ? WHERE UserID = 69", -delta)

            else:
                await ctx.send("You have to guess either h or t")
        else:
            await ctx.send(self.broketext)

    @command(aliases=['hb'])
    async def housebank(self,ctx):
        numleaves = db.record("SELECT XP FROM userXP WHERE UserID = 69")
        if (numleaves[0] >= 0):
            await ctx.send(f"Lol I've won {numleaves[0]} leaves from you scrubs")
        else:
            await ctx.send(f"Y'all have won {-numleaves[0]} leaves from me :c")

    @command()
    async def giveleaf(self, ctx, target: discord.Member, amount):
        numleaves = db.record("SELECT XP FROM userXP WHERE UserID = ?", ctx.author.id)
        if (numleaves[0] > int(amount)):
            db.execute("UPDATE userXP SET XP = XP - ? WHERE UserID = ?", amount, ctx.author.id)
            db.execute("UPDATE userXP SET XP = XP + ? WHERE UserID = ?", amount, target.id)
            await ctx.send(f"Successfuly given {amount} leaves to {target.name}")
        else:
            await ctx.send(self.broketext)
        

def setup(bot):
    bot.add_cog(LeafGames(bot))