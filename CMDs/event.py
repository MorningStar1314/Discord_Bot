import discord
from discord.ext import commands
from Core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    #成員加入
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['announce_channel']))
        await channel.send(f'{member} join!!')
        print(f'{member} join!!')


    #成員離開
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['announce_channel']))
        await channel.send(f'{member} leave!!')
        print(f'{member} leave!!')

    

    @commands.Cog.listener()
    async def on_message(self,msg):
        Keyword = ['apple','pen']
        if msg.content in Keyword and msg.author != self.bot.user: #完整字元
            await msg.channel.send('hi')
        if msg.content.endswith in Keyword and msg.author != self.bot.user:  #結尾擁有的字元
            await msg.channel.send('hi')

def setup(bot):
    bot.add_cog(Event(bot))