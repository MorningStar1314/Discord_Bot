#導入Discord.py
import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.all()

#建置Bot實體，設定命令符號
bot=commands.Bot(command_prefix='[',intents=intents)

#上線
@bot.event
async def on_ready():
    print(">> Bot is online <<")


#成員加入
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['announce_channel']))
    await channel.send(f'{member} join!!')
    print(f'{member} join!!')


#成員離開
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['announce_channel']))
    await channel.send(f'{member} leave!!')
    print(f'{member} leave!!')


#Ping指令
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')




bot.run(jdata['TOKEN'])