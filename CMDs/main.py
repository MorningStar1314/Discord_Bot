import discord
from discord.ext import commands
from Core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):

    #Ping指令
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    #hi
    @commands.command()
    async def hi(self,ctx):
        await ctx.send("嗨嗨")

    #em
    """@commands.command()
    async def em(self,ctx):"""

    #訊息複誦
    @commands.command()
    async def sayd(self,ctx,msg):
        await ctx.message.delete()
        await ctx.send(msg)



def setup(bot):
    bot.add_cog(Main(bot))