import discord

from discord.ext import commands

class Quiz(commands.Cog):
    print("==> Cog Loaded: Quiz")
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def quiz(self, ctx):
        """Quiz yourself on the different models of Chromebooks!"""

        print('hi')
        await ctx.respond('worked')
        
def setup(bot):
    bot.add_cog(Quiz(bot))