import discord
from discord.ext import commands

from Core.classes import Cog_Extension

class Main(Cog_Extension):

    #Ping指令
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    #hi
    @commands.command()
    async def hi(self,ctx):
        await ctx.send("嗨嗨")

def setup(bot):
    bot.add_cog(Main(bot))