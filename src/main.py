#!/usr/bin/python3
from discord.ext import commands
import random
import re
import os
import sys


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('DISCORD_ACCESS_TOKEN')

roll_pattern = re.compile(r'[0-9]+d[0-9]+', re.IGNORECASE)


@bot.command()
async def roll(ctx, arg):
    if(roll_pattern.match(arg)):
        result = []
        times, dots = map(int, arg.split('d'))
        for i in range(times):
            result.append(random.randint(1, dots))

        output = "\n実行：%s\n結果：%d\n[%s]" % (arg, sum(result), ', '.join(map(str, result)))
        await ctx.send(format(ctx.author.mention) + output)
    else:
        await ctx.send('\nError!\n[振る個数]d[ダイスの種類]で指定してください(例：2d6)')


@bot.command()
async def match(ctx):
    if hasattr(ctx.message.author.voice, 'channel'):
        matchList = []
        if 2 <= len(ctx.message.author.voice.channel.members):
            matchList = random.sample(ctx.message.author.voice.channel.members, 2)
        else:
            await ctx.send("ふたり以上のユーザーが必要です")
            return

        output = "対戦:\n"
        for m in matchList:
            output = output + format(m.mention) + '\n'
        await ctx.send(output)
    else:
        await ctx.send("ボイスチャンネルに入った状態でコマンドを実行してください")


if __name__ == "__main__":
    if token is None:
        sys.exit("TOKEN IS EMPTY!")

    bot.run(token)
