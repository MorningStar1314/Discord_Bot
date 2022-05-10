#導入Discord.py
import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

#建置Bot實體，設定命令符號
bot = commands.Bot(command_prefix='[',intents=intents)

#上線
@bot.event
async def on_ready():
    print(">> Bot is online <<")


#成員加入
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['announce_channel']))
    await channel.send(f'{member} join!!')
    print(f'{member} join!!')


#成員離開
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['announce_channel']))
    await channel.send(f'{member} leave!!')
    print(f'{member} leave!!')


#載入
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'CMDs.{extension}')
    await ctx.send(f'Loaded {extension} done.')

#卸載
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'CMDs.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

#重新載入
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'CMDs.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

for Filename in os.listdir('./CMDs'):
    if Filename.endswith('.py'):
        bot.load_extension(F'CMDs.{Filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])