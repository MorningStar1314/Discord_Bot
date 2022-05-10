import discord
from discord.ext import commands
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

from Core.classes import Cog_Extension

class React(Cog_Extension):
    #傳照片(主機路徑)
    @commands.command()
    async def 隨機圖片(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(random_pic)


    #傳照片(網址)
    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))